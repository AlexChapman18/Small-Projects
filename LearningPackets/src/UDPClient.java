import java.io.IOException;
import java.net.*;

public class UDPClient implements Runnable {

    private final int port;

    public UDPClient(int port) {
        this.port = port;
    }


    public void run(){
        try {
            System.out.println("Client started");
            DatagramSocket clientSocket = new DatagramSocket(port);
            byte[] buffer = new byte[65507];

            // If you dont recive anything, will throw exception and shutdown client.
            clientSocket.setSoTimeout(3000);
            while(true){
                DatagramPacket datagramPacket = new DatagramPacket(buffer, 0, buffer.length);
                clientSocket.receive(datagramPacket);

                String recievedMessage =new String(datagramPacket.getData());
                System.out.println(recievedMessage);
            }

        } catch (SocketException ignored) {} catch (IOException e) {
            System.out.println("Has timed out");
        }
    }
}
