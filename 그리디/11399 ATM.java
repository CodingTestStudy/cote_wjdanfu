import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N=scan.nextInt();
		
		int[] man=new int[N];
		
		for(int i=0;i<man.length;i++) {
			man[i]=scan.nextInt();	
			
		}
		Arrays.sort(man);
		int sum = 0,result=0;
		for(int i=0;i<man.length;i++) {
		
			sum+=man[i];
			result+=sum;
		}
		
		System.out.print(result);
	}
}

/* 
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sca = new Scanner(System.in);
        int num= sca.nextInt();
        int time[]=new int[num];
        for(int i=0;i<num;i++) {
        	time[i]=sca.nextInt();        	
        }
        Arrays.sort(time);
        int sum=0;
        int n[]=new int [num];
        for(int i=0;i<num;i++) {
        	sum+=time[i];
        	n[i]=sum;
        }
        int result=0;
        for(int i=0;i<num;i++) {
        	result+=n[i];
        }
        System.out.print(result);
       
    }
}
*/
