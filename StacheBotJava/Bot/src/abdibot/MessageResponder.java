package abdibot;

import java.util.Random;

import com.sedmelluq.discord.lavaplayer.player.AudioPlayer;
import com.sedmelluq.discord.lavaplayer.player.event.AudioEvent;
import com.sedmelluq.discord.lavaplayer.player.event.AudioEventListener;
import com.sedmelluq.discord.lavaplayer.source.AudioSourceManagers;

import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;
import net.dv8tion.jda.core.managers.AudioManager;
import net.dv8tion.jda.core.audio.AudioSendHandler;
import net.dv8tion.jda.core.entities.Guild;
import net.dv8tion.jda.core.entities.Member;
import net.dv8tion.jda.core.entities.VoiceChannel;
import net.dv8tion.jda.core.events.guild.*;
import com.sedmelluq.discord.lavaplayer.player.*;
import com.sedmelluq.discord.lavaplayer.source.youtube.YoutubeAudioTrack;
import com.sedmelluq.discord.lavaplayer.tools.FriendlyException;
import com.sedmelluq.discord.lavaplayer.track.AudioPlaylist;
import com.sedmelluq.discord.lavaplayer.track.AudioTrack;


public class MessageResponder extends ListenerAdapter {
	
	public void onMessageReceived(MessageReceivedEvent event)
	{
		
		String message = event.getMessage().getContent();
		
		if(message.contains("jeff"))
		{
			String name = event.getAuthor().getName();
			
			event.getTextChannel().sendMessage("HAHA FUNNY MEME, " + name).queue();
		}
		if(message.contains("dinlo") || message.contains("ass") || message.contains("faggot") || message.contains("fuck") || message.contains("gay") || message.contains("nigger") || message.contains("gay"))
		{
			event.getTextChannel().sendMessage("AY, NO BAD WORDS IN MY CHRISTIAN DISCORD!").queue();
		}
		if(message.contains("!roll"))
		{
			Random random = new Random();
			
			int j = random.nextInt(20);
			
			String p = new Integer(j).toString();
			
			event.getTextChannel().sendMessage(p).queue();
		}
		if(message.startsWith("!play"))
		{
			String search = message.replaceAll("!play ", "");
			System.out.println(search);
			Member member = event.getMember();
			
			
			

			
			AudioPlayerManager playerManager = new DefaultAudioPlayerManager();
			AudioSourceManagers.registerRemoteSources(playerManager);

			
			
			System.out.println(member);
			VoiceChannel mychannel = member.getVoiceState().getChannel();
			Guild guild = event.getGuild();
			AudioManager audiomanager = guild.getAudioManager();
			AudioPlayer audio = playerManager.createPlayer();	
			TrackScheduler trackscheduler = new TrackScheduler(audio);
			audio.addListener(trackscheduler);
			
			
			audiomanager.setSendingHandler(new AudioPlayerSendHandler(audio));
			audiomanager.openAudioConnection(mychannel);
			playerManager.loadItem(search, new AudioLoadResultHandler() {
				  @Override
				  public void trackLoaded(AudioTrack track) {
				    trackscheduler.queue(track);
				  }

				@Override
				public void loadFailed(FriendlyException arg0) {
					// TODO Auto-generated method stub
					
				}

				@Override
				public void noMatches() {
					// TODO Auto-generated method stub
					
				}

				@Override
				public void playlistLoaded(AudioPlaylist arg0) {
					// TODO Auto-generated method stub
					
				}
				
			});
			
			

			
		
		
		
	}

		if(message.contains("!stop"))
		{
			Guild guild = event.getGuild();
		AudioManager audiomanager = guild.getAudioManager();

		audiomanager.closeAudioConnection();
		}

}
}
