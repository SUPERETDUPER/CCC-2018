import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.valueOf(scanner.nextLine());

        Integer[][] matrix = new Integer[N][N];

        for (int y = 0; y < N; y++) {
            String row = scanner.nextLine();
            String[] splitRow = row.split(" ");
            for (int x = 0; x < N; x++) {
                matrix[y][x] = Integer.valueOf(splitRow[x]);
            }
        }

        if (matrix[0][0] > matrix[0][1] && matrix[0][0] > matrix[1][0]) {
            print180(matrix);
        } else if (matrix[0][0] > matrix[0][1]) {
            print270(matrix);
        } else if (matrix[0][0] > matrix[1][0]) {
            print90(matrix);
        } else {
            print360(matrix);
        }
    }

    private static void print360(Integer[][] matrix) {
        for (int y = 0; y < matrix.length; y++) {
            for (int x = 0; x < matrix.length; x++) {
                System.out.print(matrix[y][x] + " ");
            }
            System.out.println();
        }
    }

    private static void print90(Integer[][] matrix) {
        for (int x = 0; x < matrix.length; x++) {
            for (int y = matrix.length - 1; y >= 0; y--) {
                System.out.print(matrix[y][x] + " ");
            }
            System.out.println();
        }
    }


    private static void print180(Integer[][] matrix) {
        for (int y = matrix.length - 1; y >= 0; y--) {
            for (int x = matrix.length - 1; x >= 0; x++) {
                System.out.print(matrix[y][x] + " ");
            }
        }
    }

    private static void print270(Integer[][] matrix) {
        for (int x = matrix.length - 1; x >= 0; x--) {
            for (int y = 0; y < matrix.length; y++) {
                System.out.print(matrix[y][x] + " ");
            }
            System.out.println();
        }
    }
}
