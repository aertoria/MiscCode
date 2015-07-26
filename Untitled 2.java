

class Untitled {
	public static void main(String[] args) {
		A a = new A();
		A b = new A();
		
		a.var=15;
		System.out.println(a.var);
		System.out.println(b.var);
	}
}




class A{
	static int var=0;
}