import java.io.IOException;
import java.net.*;

public class UDPServer implements Runnable {

    private final int port;

    public UDPServer(int port) {
        this.port = port;
    }


    public void run(){
        try {
            System.out.println("Server started");
            DatagramSocket serverSocket = new DatagramSocket(port);
            for (int i = 0; i < 3; i++){
                String message = "hello" + i;
                DatagramPacket serverPacket = new DatagramPacket(
                        message.getBytes(),
                        message.length(),
                        InetAddress.getLocalHost(),
                        port
                );
                System.out.println("packet sent: " + i);
                serverSocket.send(serverPacket);
            }

        } catch (IOException a) {
            System.out.println(a);
        }
    }
}
