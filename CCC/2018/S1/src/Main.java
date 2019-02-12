import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int nVillages = scanner.nextInt();

        ArrayList<Integer> villages = new ArrayList<Integer>();

        for (int i = 0; i < nVillages; i++) {
            villages.add(scanner.nextInt());
        }

        villages.sort(null);

        float smallest = Float.MAX_VALUE;
        float previousBorder = Float.MIN_VALUE;

        for (int i = 1; i < villages.size(); i++) {
            float border = (villages.get(i - 1) + villages.get(i)) / 2;

            if (previousBorder != Float.MIN_VALUE) {
                if (border - previousBorder < smallest) {
                    smallest = border - previousBorder;
                }
            }

            previousBorder = border;
        }

        System.out.println(smallest);

    }
}