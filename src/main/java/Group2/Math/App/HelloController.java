/* So this class is what is showing the webpage. Here is where we will have our html templates.
 */
package Group2.Math.App;

import Services.MathAppService;


// I don't really know what these are and why they need to be there but it works.
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
public class HelloController {

    @Autowired
    private MathAppService mathAppService;
    @GetMapping("/")
    public String helloWorld() {
        // return "index"; will display the index.html file which is in the resources/templates folder.
        return "math";

    }

    @PostMapping("/")
    public String processUserInput(@RequestParam("userInput") String userInput, RedirectAttributes redirectAttributes) {
        // Call the MathAppService to process the user input
        String processedOutput = mathAppService.processInput(userInput);

        // Add a flash attribute to pass the processed output to the redirected GET request
        redirectAttributes.addFlashAttribute("userInput", processedOutput);

        // Redirect back to the root path ("/") to refresh the page with the updated content
        return "redirect:/";
    }

    @GetMapping("/math")
    public String math() {
        return "math";
    }

}
