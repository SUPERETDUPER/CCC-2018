import java.util.Scanner;

public class Main {


    private static boolean[][] cameraDanger;
    private static int N = 5;
    private static int M = 7;

    private static final char WALL = 'W';
    private static final char UP = 'U';
    private static final char DOWN = 'D';
    private static final char RIGHT = 'R';
    private static final char LEFT = 'L';
    private static final char EMPTY = '.';
    private static final char START = 'S';
    private static final char CAMERA = 'C';

    private static char[][] matrix = {
            {WALL, WALL, WALL, WALL, WALL, WALL, WALL},
            {WALL, DOWN, EMPTY, LEFT, EMPTY, RIGHT, WALL},
            {WALL, EMPTY, WALL, CAMERA, UP, EMPTY, WALL},
            {WALL, WALL, WALL, EMPTY, START, EMPTY, WALL},
            {WALL, WALL, WALL, WALL, WALL, WALL, WALL},
    };

    private static final boolean useInput = false;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (useInput) {
            N = scanner.nextInt();
            M = scanner.nextInt();
            scanner.nextLine();

            matrix = new char[N][M];

            for (int y = 0; y < N; y++) {
                matrix[y] = scanner.nextLine().toCharArray();
            }
        }

        Coord starting = null;
        cameraDanger = new boolean[N][M];

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

        if (starting == null) {
            System.out.println("Invalid input; no starting");
            return;
        }

        int[][] results = new int[N][M];

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                results[y][x] = -1;
            }
        }

        results = run(starting, results, 0);

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (matrix[y][x] == EMPTY) {
                    if (results[y][x] == 0) {
                        System.out.println(-1);
                    } else {
                        System.out.println(results[y][x]);
                    }
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
                case WALL:
                    keepGoing = false;
                    break;
                case EMPTY:
                    cameraDanger[y][camera.x] = true;
                    break;
            }
        }
    }

    private static int[][] run(Coord currentPose, int[][] past, int steps) {
        if (matrix[currentPose.y][currentPose.x] == WALL) {
            return past;
        } else if (past[currentPose.y][currentPose.x] != -1 && past[currentPose.y][currentPose.x] <= steps) {
            return past;
        } else if (cameraDanger[currentPose.y][currentPose.x]) {
            return past;
        } else if (currentPose.y >= N || currentPose.x >= M) {
            return past;
        }

        past[currentPose.y][currentPose.x] = steps;

        switch (matrix[currentPose.y][currentPose.x]) {
            case UP:
                return run(currentPose.getShiftUp(), past, steps);
            case DOWN:
                return run(currentPose.getShiftDown(), past, steps);
            case RIGHT:
                return run(currentPose.getShiftRight(), past, steps);
            case LEFT:
                return run(currentPose.getShiftLeft(), past, steps);
            case START:
            case EMPTY:
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
            return new Coord(x, y + 1);
        }

        Coord getShiftUp() {
            return new Coord(x, y - 1);
        }
    }
}
