public class MultithreadThing implements Runnable{

    private int threadNumber;
    public MultithreadThing(int _number){
        this.threadNumber = _number;
    }
    @Override
    public void run(){
        for(int i = 0; i < 5; i++){
            System.out.println(i + "From thread" + threadNumber);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
            }
        }
    }
}
