import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N=scan.nextInt();
		int M=scan.nextInt();
		int K=scan.nextInt();
		int[] arr = new int[N];
		
		for(int i = 0; i < arr.length; i++)
			arr[i] = scan.nextInt();
		Arrays.sort(arr);
		int sum=0;
		while(M>0) {
			for(int i=0; i<K; i++) {
				sum+=arr[arr.length-1];
				M--;
			}
			sum+=arr[arr.length-2];
			M--;
		}
	System.out.print(sum);
	}
}
