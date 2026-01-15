import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        int num = Integer.parseInt(st.nextToken());
        int max = num;
        int min = num;

        for (int i = 1; i < n; i++) {
            num = Integer.parseInt(st.nextToken());

            if (max < num) max = num;
            if (min > num) min = num;
        }

        sb.append(min).append(" ").append(max).append("\n");

        System.out.println(sb);
    }
}
