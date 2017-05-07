package mock;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class AllLinks {

	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver", "./driver/chromedriver.exe");
		WebDriver driver=new ChromeDriver();
		driver.get("file:///F:/pages/links.html");
List<WebElement> allLinks=driver.findElements(By.xpath("//a"));
for(WebElement link:allLinks)
	System.out.println(link.getText());
	}

}
