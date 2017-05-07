package mock;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class DuplicatLink {
	
	public static ArrayList<String> getIntoStringArrayList(WebElement select)
	{
		Select listbox=new Select(select);
		List<WebElement> allOptions=listbox.getOptions();
		ArrayList<String> allTexts=new ArrayList<String>();
		for(WebElement option:allOptions)
			allTexts.add(option.getText());
		return allTexts;
	}

	public static void main(String[] args) {
		System.setProperty("webdriver.gecko.driver", "./driver/geckodriver.exe");
		WebDriver driver=new FirefoxDriver();
		driver.get("file:///F:/pages/listbox2.html");
		
		WebElement select=driver.findElement(By.id("mtr"));
		
		ArrayList<String> allTexts=getIntoStringArrayList(select);
		
		HashSet<String> items=new HashSet<String>();
		
		for(String allText:allTexts)
		{
			if(!items.add(allText))
				System.out.println(allText);
		}
		

	}

}
