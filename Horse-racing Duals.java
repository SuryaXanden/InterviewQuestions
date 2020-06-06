import java.util.*;
class Solution {
    public static void main(final String args[]) {
        final Scanner in = new Scanner(System.in);
        final int N = in.nextInt();
		int d, m = 100000;
        int indexes[] = new int[N];
        for (int i = 0; i < N; i++) {
            indexes[i] = in.nextInt();
        }
        Arrays.sort(indexes);
        for (int i = 0; i < N-1; i++) {
            d = indexes[i+1] - indexes[i];
            if (d < m) {
                m = d;
            }
        }
        System.out.println(m);
        in.close();
    }
}
