import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class HelloWorldClient {

    public static void main(String[] args) {

        String firstname = args.length > 0 ? args[0] : "Max";
        String lastname  = args.length > 1 ? args[1] : "Mustermann";

        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 50051)
                .usePlaintext()
                .build();

        HelloWorldServiceGrpc.HelloWorldServiceBlockingStub stub = HelloWorldServiceGrpc.newBlockingStub(channel);
        Hello.ProductData product1 = Hello.ProductData.newBuilder()
                .setProductId("00-443175")
                .setProductName("Bio Orangensaft Sonne")
                .setProductCategory("Getraenk")
                .setProductQuantity(1500)
                .setProductUnit("Packung 1L")
                .build();

        Hello.ProductData product2 = Hello.ProductData.newBuilder()
                .setProductId("02-341867")
                .setProductName("Milka Tafel")
                .setProductCategory("Sueßigkeit")
                .setProductQuantity(1000)
                .setProductUnit("Packung 500g")
                .build();

        Hello.WarehouseData warehouse = Hello.WarehouseData.newBuilder()
                .setWarehouseID("001")
                .setWarehouseName("Linz Bahnhof")
                .setWarehouseAddress("Bahnhofpl. 3-6")
                .setWarehouseCity("Linz")
                .setWarehouseCountry("Österreich")
                .setWarehousePostalCode(4020)
                .addProductData(product1)
                .addProductData(product2)
                .build();

        stub.sendWarehouseData(warehouse);
        System.out.println("Send information of Warehouse data");
        channel.shutdown();

    }

}
