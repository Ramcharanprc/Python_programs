// Connection to a Python socket using Java client.
import java.io.*;
import java.net.*;
import java.util.*;

public class client
{
	public static void main(String args[])
	{
		try
		{
			Scanner readInput = new Scanner(System.in);
			System.out.print("Enter IP address: ");
			String userIp = readInput.nextLine();
			System.out.print("Enter Port number: ");
			int port = readInput.nextInt();
			Socket socketObj = new Socket(userIp, port);
			InputStreamReader dataOut = new InputStreamReader(socketObj.getInputStream());
			BufferedReader readData = new BufferedReader(dataOut);
			String message = readData.readLine();
			System.out.println(message);
			dataOut.close();
			socketObj.close();
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}
}