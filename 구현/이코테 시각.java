import java.util.*;
import java.io.*;

public class Main {
	public static boolean count(int i,int j, int k){
		if (i/10==3|| i % 10 == 3 || j / 10 == 3 || j % 10 == 3 || k / 10 == 3 || k % 10 == 3)
            return true;
        return false;
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
		int N= Integer.parseInt(br.readLine());
		int sum=0;
		for(int i=0;i<N+1;i++) {
			for(int j=0;j<60;j++) {
				for(int k=0;k<60;k++) {
					if(count(i,j,k))
						sum++;
				}
				
			}
			
		}
		System.out.print(sum);
		
	}
}

/*for(int i=0;i<N+1;i++) {
			for(int j=0;j<60;j++) {
				for(int k=0;k<60;k++) {
					if(k%10==3||k/10==3)
						sum++;
				}
				if(j%10==3||j/10==3)
					sum++;
			}
			if(i%10==3||i/10==3)
				sum++;
		}
 이런 방식보다 중복을 피해기 위해 함수를 만들어서 쓰는 연습을 하자! */
