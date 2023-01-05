public class Multithreading{
    public static void main(String[] args) {


        for (int i = 0; i < 5; i++){
            MultithreadThing myThing = new MultithreadThing(i);
            Thread myThread = new Thread(myThing);
//        Use start to start the thread, using run will run code un-threaded
            myThread.start();
        }
    }
}
