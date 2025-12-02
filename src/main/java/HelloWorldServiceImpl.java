import io.grpc.stub.StreamObserver;

public class HelloWorldServiceImpl extends HelloWorldServiceGrpc.HelloWorldServiceImplBase {

    @Override
    public void hello( Hello.HelloRequest request, StreamObserver<Hello.HelloResponse> responseObserver) {

        System.out.println("Handling hello endpoint: " + request.toString());

        String text = "Hello World, " + request.getFirstname() + " " + request.getLastname();
        Hello.HelloResponse response = Hello.HelloResponse.newBuilder().setText(text).build();

        responseObserver.onNext(response);
        responseObserver.onCompleted();

    }

    @Override
    public void sendWarehouseData(Hello.WarehouseData request, StreamObserver<Hello.WarehouseResponse> responseObserver) {

        System.out.println("WarehouseID: " + request.getWarehouseID());
        System.out.println("Warehouse Name: " + request.getWarehouseName());
        System.out.println("Adresse: " + request.getWarehouseAddress());
        System.out.println("Stadt: " + request.getWarehouseCity());
        System.out.println("Land: " + request.getWarehouseCountry());
        System.out.println("PLZ: " + request.getWarehousePostalCode());
        System.out.println("Produkte:");

        for (Hello.ProductData p : request.getProductDataList()) {
            System.out.println("- " + p.getProductName() +
                    " | Kategorie: " + p.getProductCategory() +
                    " | Menge: " + p.getProductQuantity() +
                    " | Einheit: " + p.getProductUnit());
        }
        Hello.WarehouseResponse response = Hello.WarehouseResponse.newBuilder().build();

        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}
