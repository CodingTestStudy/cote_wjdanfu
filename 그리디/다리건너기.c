#include<stdio.h>
#include<stdlib.h>
#include <stdbool.h>
int main(void){
    int people;
    printf("몇명인지 입력후 사람수대로 각자 속도 입력 : ");
    scanf("%d", &people);
    int *speed = malloc(sizeof(int) * people); 
    for (int i = 0; i < people; i++)       
    {
        scanf("%d", &speed[i]);            
    }
     // 버블정렬
    int temp = 0;
    for (int i = 0; i < people; i++) {
        bool changed = false;
        for (int j = 0; j < people - 1; j++) {
            if (speed[j] > speed[j + 1]) {
                temp = speed[j];
                speed[j] = speed[j + 1];
                speed[j + 1] = temp;
                changed = true;
            }
        }
        if (!changed) break;
    }

    int result = 0;
    for (int i = people; i > 2; i-=2)       // 한싸이클마다 두사람이 지나가므로 i-=2 
    {
        if(i == 3){                          //people이 홀수 일때만 적용
            result += speed[0]+speed[2];    //홀수일때 1,3번 보내고 1번 돌아오는 시간
            printf("%d %d\n", speed[0],speed[2]);
            printf("%d\n",speed[0]);
            break;
        }
        result += speed[0]+speed[1]+speed[i-1]+speed[1]; //한싸이클에 걸리는 시간
        printf("%d %d\n", speed[0], speed[1]);
        printf("%d\n", speed[0]);
        printf("%d %d\n", speed[i-2], speed[i-1]);
        printf("%d\n", speed[1]);
    }
    result += speed[1];     //i가 2이면 반복 탈출후 1번과2번만 남았으므로 2번시간만 더한후 출력
    printf("%d %d\n", speed[0],speed[1]);
    printf("최단시간 : %d\n", result);
    free(speed);  
}
