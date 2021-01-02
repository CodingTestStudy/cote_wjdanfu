import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
		int N= Integer.parseInt(br.readLine());
		String[] a = br.readLine().split(" "); 
		int x=1,y=1;
		int[] dx= {0, 0, -1, 1};
		int[] dy= {1, -1, 0, 0};
		char[] alp= {'R','L','U','D'};
		for(int i=0;i<a.length;i++) {
			char b= a[i].charAt(0);
			for(int j=0;j<4;j++) {
				if(b==alp[j]) {
					x=x+dx[j];
					y=y+dy[j];
				}
			}
			if(x<=0)
				x++;
			if(y<=0)
				y++;
			if(x>N)
				x--;
			if(y>N)
				y--;
		}
		bw.write(x+" "+y);
		bw.close();//스트림을 닫음
		
	}
}
/* BufferedReader, BufferedWriter를 사용해보았다.
익숙해지자!
문제구현은 패턴을 외우면 될거같다
*/
