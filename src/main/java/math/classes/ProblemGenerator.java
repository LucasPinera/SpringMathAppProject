package math.classes;

import java.util.Random;

public class ProblemGenerator {

    private static final Random RANDOM = new Random();

    public Problem generateProblem() {
        int a = RANDOM.nextInt(10) + 1;
        int b = RANDOM.nextInt(10) + 1;
        int c = RANDOM.nextInt(10) + 1;

        String problemText = String.format("%d + %d * %d", a, b, c);
        String correctAnswer = Integer.toString(a + b * c);

        return new Problem(problemText, correctAnswer);
    }
}
