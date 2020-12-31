import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N=scan.nextInt();
		int K=scan.nextInt();
		int sum=0;
		while(N>1)
		if(N%K!=0) {
			N--;
			sum++;
		}
		else {
			N/=K;
			sum++;
		}
		System.out.print(sum);
	}
}
