package math.classes;

public class Main {

    public static void main(String[] args) {
        ProblemGenerator problemGenerator = new ProblemGenerator();

        for (int i = 0; i < 10; i++) {
            Problem problem = problemGenerator.generateProblem();
            System.out.println("Problem: " + problem.getProblemText());
            System.out.println("Answer: " + problem.getCorrectAnswer());
        }

    }
}
