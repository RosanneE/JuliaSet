import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;

/*
 * Julia set program
 * Rosanne Anderson
 */

public class JuliaSet extends JFrame{

	public final double XSCALE = .0035;
	public final double YSCALE = .0035;
	public final double XOFFSET = -525.0;
	public final double YOFFSET = -400.0;
	public final double C = .285;
	
	public JuliaSet(){
		setSize(1000, 1000);
		setVisible(true);
	}

	public static void main(String args[]){
		new JuliaSet();
	}
	/*
	 * Tests each pixel to determine if it is in the Julia set, then colors it 
	 * accordingly.  
	 * (non-Javadoc)
	 * @see java.awt.Window#paint(java.awt.Graphics)
	 */
	public void paint(Graphics g){
		for (int i = 0; i < 1000; i++){
			for (int j = 0; j < 1000; j ++){
				int newjul = julia(i,j);
				if (newjul > 20){
					g.setColor(new Color(100, 100, (int ) (255 - newjul*2.5)));
				} else {
					g.setColor(new Color( (int) (255 - (newjul*2.5)), 0, 250));
				}
				g.drawRect(i, j, 1, 1);
			}
		}
	}
	/*
	 * Tests to determine if (i,j) is in the Julia set)
	 */

	public int julia(double i,double j){
		i = (i + XOFFSET) * XSCALE;
		j = (j + YOFFSET) * YSCALE;
		double newi = i;
		double newj = j;

		for (int x = 0; x < 100; x++){
			newi = ((i*i) - (j*j) + C);
			newj = 2 * i * j;
			i = newi;
			j = newj;
			if (newi*newi + newj*newj > 100){
				return x;
			}
		}
		return 100;
	}
}

