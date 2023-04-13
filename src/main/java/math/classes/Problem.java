package math.classes;


public class Problem {
    private String problemText;
    private String correctAnswer;

    public Problem(String problemText, String correctAnswer) {
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

    public String getCorrectAnswer() {
        return correctAnswer;
    }

    public void setCorrectAnswer(String correctAnswer) {
        this.correctAnswer = correctAnswer;
    }
}
