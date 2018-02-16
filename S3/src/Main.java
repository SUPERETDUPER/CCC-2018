import java.util.Scanner;

public class Main {

    private static char[][] matrix;
    private static Boolean[][] cameraDanger;
    private static int N;
    private static int M;

    private static final char WALL = "W".charAt(0);
    private static final char UP = "U".charAt(0);
    private static final char DOWN = "D".charAt(0);
    private static final char RIGHT = "R".charAt(0);
    private static final char LEFT = "L".charAt(0);
    private static final char EMPTY = ".".charAt(0);
    private static final char START = "S".charAt(0);
    private static final char CAMERA = "C".charAt(0);

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();

        matrix = new char[N][M];

        for (int y = 0; y < N; y++) {
            matrix[y] = scanner.nextLine().toCharArray();
        }

        Coord starting = null;
        cameraDanger = new Boolean[N][M];

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (matrix[y][x] == CAMERA) {
                    markDanger(new Coord(x, y));
                }
                if (matrix[y][x] == START) {
                    starting = new Coord(x, y);
                }
            }
        }

        if (starting == null){
            System.out.println("Invalid input; no starting");
            return;
        }

        int[][] result = run(starting, new int[N][M], 0);

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                if (matrix[y][x] == START){
                    System.out.println(result[y][x]);
                }

            }
        }
    }

    private static void markDanger(Coord camera) {
        cameraDanger[camera.y][camera.x] = true;

        boolean keepGoing = true;
        for (int x = camera.x; x < M && keepGoing; x++) {
            switch (matrix[camera.y][x]) {
                case WALL:
                    keepGoing = false;
                    break;
                case EMPTY:
                    cameraDanger[camera.y][x] = true;
                    break;
            }
        }

        keepGoing = true;
        for (int x = camera.x; x >= 0 && keepGoing; x--) {
            switch (matrix[camera.y][x]) {
                case WALL:
                    keepGoing = false;
                    break;
                case EMPTY:
                    cameraDanger[camera.y][x] = true;
                    break;
            }
        }

        keepGoing = true;
        for (int y = camera.y; y < N && keepGoing; y++) {
            switch (matrix[y][camera.x]) {
                case WALL:
                    keepGoing = false;
                    break;
                case EMPTY:
                    cameraDanger[y][camera.x] = true;
                    break;
            }
        }

        keepGoing = true;
        for (int y = camera.y; y >= 0 && keepGoing; y--) {
            switch (matrix[y][camera.x]) {
                case "W":
                    keepGoing = false;
                    break;
                case ".":
                    cameraDanger[y][camera.x] = true;
                    break;
            }
        }
    }

    private static int[][] run(Coord currentPose, int[][] past, int steps) {
        if (matrix[currentPose.y][currentPose.x].equals("W")) {
            return past;
        } else if (past[currentPose.y][currentPose.x] != 0 && past[currentPose.y][currentPose.x] <= steps) {
            return past;
        } else if (cameraDanger[currentPose.y][currentPose.x]) {
            return past;
        } else if (currentPose.y >= N || currentPose.x >= M) {
            return past;
        }

        past[currentPose.y][currentPose.x] = steps;

        switch (matrix[currentPose.y][currentPose.x]) {
            case "U":
                return run(currentPose.getShiftUp(), past, steps);
            case "D":
                return run(currentPose.getShiftDown(), past, steps);
            case "R":
                return run(currentPose.getShiftRight(), past, steps);
            case "L":
                return run(currentPose.getShiftLeft(), past, steps);
            case ".":
                past = run(currentPose.getShiftLeft(), past, steps + 1);
                past = run(currentPose.getShiftRight(), past, steps + 1);
                past = run(currentPose.getShiftDown(), past, steps + 1);
                past = run(currentPose.getShiftUp(), past, steps + 1);
        }
        return past;
    }


    private static class Coord {
        final int x;
        final int y;

        Coord(int x, int y) {
            this.x = x;
            this.y = y;
        }

        Coord getShiftLeft() {
            return new Coord(x - 1, y);
        }

        Coord getShiftRight() {
            return new Coord(x + 1, y);
        }

        Coord getShiftDown() {
            return new Coord(x, y - 1);
        }

        Coord getShiftUp() {
            return new Coord(x, y + 1);
        }
    }
}
