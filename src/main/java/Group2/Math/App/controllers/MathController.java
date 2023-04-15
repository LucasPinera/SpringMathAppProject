package Group2.Math.App.controllers;

import math.classes.*;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MathController {

    @PostMapping("/process-choice")
    public String processUserChoice(@RequestParam("choice") String choice) {
        // Process user input and call appropriate functions based on the choice
        switch (choice) {
            case "a":
                // Execute code for option A
                System.out.println("User picked a");
                break;
            case "b":
                // Execute code for option B
                System.out.println("User picked b");
                break;
            case "c":
                // Execute code for option C
                System.out.println("User picked c");
                break;
            case "d":
                // Execute code for option D
                System.out.println("User picked d");
                break;
            default:
                // Handle invalid input
                break;
        }

        // Return a response (e.g., success message, next question, or error message)
        return "Processed choice: " + choice;
    }
    //@GetMapping("/random-problem")
    @GetMapping(value = "/random-problem", produces = MediaType.APPLICATION_JSON_VALUE)
    public Problem getRandomProblem() {
        ProblemGenerator problemGenerator = new ProblemGenerator();
        return problemGenerator.generateProblem();
    }

    @PostMapping("/api/math/check-answer")
    public String checkAnswer(@RequestParam("problemId") String problemId, @RequestParam("userAnswer") String userAnswer) {
        // Your code to check if the provided answer is correct

        // If the answer is correct
        return "Correct!";

        // If the answer is incorrect
        // return "Incorrect!";
    }
}
