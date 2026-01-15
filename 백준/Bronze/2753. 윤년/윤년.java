import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int result = 0;

        if ((n % 4 == 0 && n % 100 != 0) || (n % 400 == 0)) {
            result = 1;
        }

        System.out.println(result);
    }
}
