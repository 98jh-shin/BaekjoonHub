import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        int repeatCount = n / 4;

        for (int i = 0; i < repeatCount; i++) {
            sb.append("long ");
        }

        sb.append("int");

        System.out.print(sb);
    }
}
