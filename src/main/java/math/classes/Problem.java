package math.classes;


public class Problem {
    private String problemText;
    private int correctAnswer;

    public Problem(String problemText, int correctAnswer) {
        this.problemText = problemText;
        this.correctAnswer = correctAnswer;
    }

    // Getters and setters

    public String getProblemText() {
        return problemText;
    }

    public void setProblemText(String problemText) {
        this.problemText = problemText;
    }

    public int getCorrectAnswer() {
        return correctAnswer;
    }

    public void setCorrectAnswer(int correctAnswer) {
        this.correctAnswer = correctAnswer;
    }
}
