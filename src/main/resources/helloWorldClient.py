import sys
import grpc

import hello_pb2 as hello_pb2
import hello_pb2_grpc as hello_pb2_grpc


def main():
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
        p1 = hello_pb2.Product(
            productID="00-443175",
            productName="Bio Orangensaft Sonne",
            productCategory="Getraenk",
            productQuantity=1500,
            productUnity="Packung 1L"
        )

        p2 = hello_pb2.Product(
            productID="02-341867",
            productName="Milka Tafel",
            productCategory="Sueßigkeit",
            productQuantity=1000,
            productUnity="Tafel 500g"
        )

        # ---- NEW: WAREHOUSE ----
        warehouse_data = hello_pb2.WarehouseData(
            warehouseID="001",
            warehouseName="Linz Bahnhof",
            warehouseAddress="Bahnhofpl. 3-6",
            warehousePostalCode=4020,
            warehouseCity="Linz",
            warehouseCountry="Österreich",
            products=[p1, p2]
        )

        # ---- SEND RPC ----
        ack = stub.sendWarehouseData(warehouse_data)
        print("Server says:", ack.status)
        print()



        # ---- FULL ATTRIBUTE OUTPUT ----
        print("=== FULL DATA SENT (Client-side) ===")
        print("WarehouseID:       ", warehouse_data.warehouseID)
        print("WarehouseName:     ", warehouse_data.warehouseName)
        print("Address:           ", warehouse_data.warehouseAddress)
        print("Postal Code:       ", warehouse_data.warehousePostalCode)
        print("City:              ", warehouse_data.warehouseCity)
        print("Country:           ", warehouse_data.warehouseCountry)
        print()

        print("Products:")
        for product in warehouse_data.products:
            print("  ------------------------------")
            print("  ProductID:      ", product.productID)
            print("  Name:           ", product.productName)
            print("  Category:       ", product.productCategory)
            print("  Quantity:       ", product.productQuantity)
            print("  Unity:          ", product.productUnity)
        print("  ------------------------------\n")


if __name__ == "_main_":
    main()