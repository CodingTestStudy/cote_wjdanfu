import java.util.Scanner;
 
public class Main {
    public static int girl,man,intern,team;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        girl= sc.nextInt();
        man=sc.nextInt();
        intern=sc.nextInt();
        if(girl>=man*2) { 
        	team=man;
        	man=0;
        	girl-=team*2;
        	}
        else {
        	team=girl/2;
        	if(girl%2==1) 
        		girl=1;        	
        	else
        		girl=0;
        	man-=team;
        }
        while(intern>0) {
        	if(man>0) {
        		man--;
        		intern--;
        	}
        	else if(girl>0) {
        		girl--;
        		intern--;
        	}
        	else if(girl>0&&man>0) {
        		girl--;
        		man--;
        		intern-=2;
        	}
        	else {
        		team--;
        		intern-=3;
        	}
        	
        }
        System.out.print(team);

        
        
    }
}
