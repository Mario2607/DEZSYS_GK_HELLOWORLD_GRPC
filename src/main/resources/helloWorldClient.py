import sys
import grpc

import hello_pb2
import hello_pb2_grpc


def main():
    print("Hello World!")
    firstname = sys.argv[1] if len(sys.argv) > 1 else "Max"
    lastname = sys.argv[2] if len(sys.argv) > 2 else "Mustermann"

    # Connect to server
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = hello_pb2_grpc.HelloWorldServiceStub(channel)

        # ---- ORIGINAL HELLO ----
        request = hello_pb2.HelloRequest(firstname=firstname, lastname=lastname)
        response = stub.hello(request)
        print()
        print(response.text)
        print()

        # ---- NEW: PRODUCTS ----
        p1 = hello_pb2.ProductData(
            productId="00-443175",
            productName="Bio Orangensaft Sonne",
            productCategory="Getraenk",
            productQuantity=1500,
            productUnit="Packung 1L"
        )

        p2 = hello_pb2.ProductData(
            productId="02-341867",
            productName="Milka Tafel",
            productCategory="Süßigkeit",
            productQuantity=1000,
            productUnit="Tafel 500g"
        )

        # ---- NEW: WAREHOUSE ----
        warehouse_data = hello_pb2.WarehouseData(
            warehouseID="001",
            warehouseName="Linz Bahnhof",
            warehouseAddress="Bahnhofpl. 3-6",
            warehousePostalCode=4020,
            warehouseCity="Linz",
            warehouseCountry="Österreich",
            productData=[p1, p2]
        )

        # ---- SEND RPC ----
        stub.sendWarehouseData(warehouse_data)
        print("Server returned a WarehouseResponse")
        print()

        # ---- FULL ATTRIBUTE OUTPUT ----
        print("WarehouseID:       ", warehouse_data.warehouseID)
        print("WarehouseName:     ", warehouse_data.warehouseName)
        print("Address:           ", warehouse_data.warehouseAddress)
        print("Postal Code:       ", warehouse_data.warehousePostalCode)
        print("City:              ", warehouse_data.warehouseCity)
        print("Country:           ", warehouse_data.warehouseCountry)
        print()

        print("Products:")
        for product in warehouse_data.productData:
            print("  ------------------------------")
            print("  ProductID:      ", product.productId)
            print("  Name:           ", product.productName)
            print("  Category:       ", product.productCategory)
            print("  Quantity:       ", product.productQuantity)
            print("  Unit:           ", product.productUnit)
        print("  ------------------------------\n")


if __name__ == "__main__":
    main()