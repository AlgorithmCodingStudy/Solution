package CodingStudy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/*
 * 세로선 개수 N, 가로선 개수 H
 * M개의 줄에는 가로선의 정보
 * i번 세로선의 결과가 i가 나오도록
 * 추가해야하는 가로선의 개수의 최소값
 * 
 * 다시
 * 
//다음처럼 미리 사다리를 두지 말자 
//		for(int row=1;row<=H;row++) {
//			for(int col=2;col<=N;col++){
//				if(ladder[row][col]==0 && ladder[row][col-1]!=1 && ladder[row][col-2]!=1) {
//					ladderList.add(new int[] {row,col-1});
//				}
//			}
//		}
 * 
 * 
 * 
 *  처음에 생각했던 것은 
 *  사다리를 설치 할 수 있는 후보군들을 조사해서 list 집합에 넣어두고
 *  조합으로 하나씩 꺼내서 검증 하는 방식을 생각했다.
 *  이때 발생하는 문제점은 다음과 같았다.
 *  사다리를 설치 하고 나서 사다리 형태가 규칙에 맞는지 확인하는 부분이 필요했다.
 *  그런데도 이미 답이 있는 경우의 케이스가 -1이 나왔다.
 *  전수조사를 했기 때문에 
 *  설치된 케이스의
 *  사다리가 정당하지 않아도 
 *  아예 불가능한 답인 -1이 아니라 
 *  정답이 있는 케이스에 대해서도 검사를 했을 것이기 때문에
 *  -1이 아닌 0~3에 대한 숫자가 나왔을텐데 답이 나오지않아 의아했다. 
 *  
 *  이후 방법을 바꿨다. 아침에 스터디에서 주영이가 했던 방법대로
 *  사다리 후보를 미리 만들어 놓고 0~3개를 뽑으면서 검증을 하는 방법이 아니라
 *  2차원 배열에서의 조합으로 dfs를 돌리는 방법으로 바꾼 뒤
 *  격자칸에 설치된 사다리의 양끝을 1,1 이라고 적지않고 왼쪽칸만 적었다.
 *  
 *  경우는 두가지다.
 *  가장 윗 행렬부터 무조건 내려가기 시작하는데
 *  1을 만나는경우는 오른쪽으로 꺾어야 하고
 *  0을 만나는 경우 왼쪽에 1이 있다면 왼쪽으로 꺾어야 하는 것이다.
 *  이 처리를 해준 뒤에도 한참동안 답이 나오지않아
 *  번아웃..상태가 되버렸다.
 *  
 *  이후
 *  다시 한줄한줄 찍어보니
 *  if문의 중괄호를 묶어주지 않은 것을 발견하고
 *  조금 어처구니없었지만... 해결했다 ㅠ 하루종일 사소한 실수로 끙끙댔다.
 *  
 */
public class 사다리조작 {
	static int N,M,H;//세로,가로,위치
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] ladder;
	static int min = Integer.MAX_VALUE;
	static boolean possible;
	public static void main(String[] args) throws IOException {
		setData();
		for(int i=0;i<=3;i++){//설치릉 안해보거나 최대 3개씩 설치해본다.
			if(possible==false) dfs(1,0,i);//row,col,depth,cnt
		}
		if(min==Integer.MAX_VALUE) System.out.println("-1");
		else System.out.println(min);
	}
	private static void dfs(int rowIdx, int depth, int cnt) {
		if(possible) return;//찾았으면 끝냄 
		if(depth==cnt){//설치했으니 확인
			check(cnt);
			return;
		}
		for(int row=rowIdx;row<=H;row++) {
			for(int col=1;col<N;col++){
				if(ladder[row][col]!=1 && ladder[row][col-1]!=1 && ladder[row][col+1]!=1) {
					ladder[row][col] = 1;
					dfs(row,depth+1,cnt);
					ladder[row][col] = 0;
				}
			}
		}
	}
	private static void check(int cnt){
		//고른 사다리 확인
		for(int i=1;i<=N;i++){//i번째부터 N번째 까지
			int col=i;
			for(int row=1;row<=H;row++){
				if(ladder[row][col]==1) col+=1;
				else if(ladder[row][col]==0 && ladder[row][col-1]==1) col-=1;
			}
			if(col==i) continue;
			else return;
		}
	
		//위 포문에서 끝났으면
		min = cnt;
		possible = true;
		return;
	}
	private static void setData() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		ladder = new int[H+1][N+1];
		for(int i=0,a,b;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			ladder[a][b] = 1; //하나만 있어도 된다
		}
	}
}
