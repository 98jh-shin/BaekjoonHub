import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int numA = Integer.parseInt(br.readLine());
        String numB = br.readLine();


        int one = numA * (numB.charAt(2) - '0');
        int ten = numA * (numB.charAt(1) - '0');
        int hundred = numA * (numB.charAt(0) - '0');
        int result = numA * Integer.parseInt(numB);

        sb.append(one).append("\n");
        sb.append(ten).append("\n");
        sb.append(hundred).append("\n");
        sb.append(result).append("\n");

        System.out.println(sb);
    }
}
