import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N=scan.nextInt();
		int M=scan.nextInt();
		int arr[][]=new int[N][M];
		int min=0;
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				arr[i][j]=scan.nextInt();
			}
		}
		for(int i=0;i<arr.length;i++) {
			Arrays.sort(arr[i]);
			if(arr[i][0]>min)
				min=arr[i][0];
		}
		System.out.print(min);
	}
}
/* 문제는 쉽지만 2차원배열에 입력할때 2중for문을 쓰는게 거슬려서 검색해보앗다.
import java.util.*;
import java.io.*;

public class Main
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int row = Integer.parseInt(st.nextToken());
        String[] minArr = new String[row];

        for(int i = 0; i < row; i++)
        {
            String s = br.readLine();
            String[] arr = s.split(" ");

            Arrays.sort(arr);

            minArr[i] = arr[0];
        }

        Arrays.sort(minArr);
        System.out.println(minArr[row-1]);
    }
}
출처 https://velog.io/@uhan2/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4.Part02.Chapter03-%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-%EA%B2%8C%EC%9E%84-Java
이분은 배열입력후 오름차순 정리하고 첫번째 원소를 minArr의 새배열로 지정했다. 그 새배열에서 최대값을 찾는방법이다.*/
