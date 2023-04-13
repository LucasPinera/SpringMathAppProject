/* So think of this as the main class of this project.
I don't know how much of this we will change.
Running this class will start the webpage. */
package Group2.Math.App;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Component;

@SpringBootApplication
@ComponentScan({"Group2.Math.App", "Services"})
public class MathAppApplication {

	public static void main(String[] args) {
		SpringApplication.run(MathAppApplication.class, args);
	}

}

//Next take a look at the 'HelloController.java' File which is in this same folder