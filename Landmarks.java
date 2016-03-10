class Landmarks
{
	public void display(String venue, String cost, String location)
	{
		System.out.println(venue + " costs $" + cost + " and is located at " + location);
	}

	public void display(String venue, int cost, String location)
	{
		System.out.println(venue + " costs $" + Integer.toString(cost) + " and is located at " + location);
	}


	public void displayAll()
	{
		display("Wrigley Field", 40, "1033 W. Addison St.");
		display("The Bean", "0", "Millenium Park.");
		display("The John Hancock Tower", "35", "875 N. Michigan Ave.");
		display("The United Center", "75", "1901 W. Madison St.");
		display("The Shakespeare Theater", "40", "Navy Pier");

	}
}
