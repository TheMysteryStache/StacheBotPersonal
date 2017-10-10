package abdibot;


import java.awt.Event;
import java.util.EventListener;

import javax.security.auth.login.LoginException;
import net.dv8tion.jda.core.AccountType;
import net.dv8tion.jda.core.JDA;
import net.dv8tion.jda.core.JDABuilder;
import net.dv8tion.jda.core.audio.*;
import net.dv8tion.jda.core.entities.Channel;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.MessageChannel;
import net.dv8tion.jda.core.entities.MessageEmbed.AuthorInfo;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.exceptions.RateLimitedException;
import net.dv8tion.jda.core.hooks.ListenerAdapter;


public class AbdiBot extends ListenerAdapter{
	
private static JDA jda;	
	
public static void main(String[] args) {

		try {
			jda = new JDABuilder(AccountType.BOT).setToken("MzYwODc0NTkzOTk4NzMzMzE0.DL1Ykw.7Ak32ekQdtwHWJ3rswBSfMWRAeE").buildAsync();
		} catch (LoginException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IllegalArgumentException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (RateLimitedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		jda.addEventListener(new MessageResponder());
	


}




}

