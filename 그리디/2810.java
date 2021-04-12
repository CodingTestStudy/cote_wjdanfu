import java.util.*;

public class Main {
	
    public static void main(String[] args) {
    	 Scanner sca=new Scanner(System.in);
    	 int N=sca.nextInt();
    	 int cup=1;
    	 String []seat=new String[N];
    	 seat=sca.next().split("");
    	 int check=0;
    	 for(int i=0;i<N;i++) {		 
    		 if(seat[i].equals("S")) 
    			 cup++;  			 
    		 else {
    			 cup++;
    			 i++;
    			 check++;
    		 }
    	 }
    	 if(check==0)
    		 System.out.print(cup-1);
    	 else
    		 System.out.print(cup);
    	 
     }
    
}
