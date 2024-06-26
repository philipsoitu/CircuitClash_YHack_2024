<main class="border-2 rounded-2xl">
   <h1 class="h1">What is Circuit Clash?</h1>
   <p>
      Circuit Clash is an online platform meant for young students and enthusiasts interested in learning about boolean logic and logic circuits. It allows you to write code in our custom language, SHDL, which is a simplified VHDL, perfect for the use of curious young enthusiasts. With Circuit Clash, you will write code, and we will draw the circuit for you in real time, allowing you to see the logic gates at work.
   </p>
   <br>
   <h1 class="h1">What is SHDL?</h1>
   <p>
      SHDL, or the Simple High-Speed Integrated Circuit Hardware Description Language, is a simplified version of VHDL. While VHDL is excellent for professional use, its strict syntax makes it less suitable as an entry point for kids learning about boolean logic. SHDL offers a more intuitive syntax, making it easier for beginners to grasp the concepts.
   </p>
   <br>
   <h1 class="h1">How does it work?</h1>
   <p>
      Before explaining the syntax for SHDL, it is better to know how logic gates work. If you already know about them you can skip to the SHDL Docs. 
   </p>
   <br>
   <h1 class="h1">Logic Gates</h1>
   <br>
   <h2 class="h2">NOT Gate</h2>
   <p>The NOT gate (also called an inverter) has only one input. It outputs the opposite state of its input.</p>
   <table>
      <thead>
         <tr>
            <th>A</th>
            <th>OUTPUT</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>0</td>
            <td>1</td>
         </tr>
         <tr>
            <td>1</td>
            <td>0</td>
         </tr>
      </tbody>
   </table>
   <br>
   <h2 class="h2">AND Gate</h2>
   <p>The AND gate outputs true (1) only when both of its inputs are true. Its truth table is:</p>
   <table>
      <thead>
         <tr>
            <th>A</th>
            <th>B</th>
            <th>OUTPUT</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>0</td>
            <td>0</td>
            <td>0</td>
         </tr>
         <tr>
            <td>0</td>
            <td>1</td>
            <td>0</td>
         </tr>
         <tr>
            <td>1</td>
            <td>0</td>
            <td>0</td>
         </tr>
         <tr>
            <td>1</td>
            <td>1</td>
            <td>1</td>
         </tr>
      </tbody>
   </table>
   <br>
   <h2 class="h2">NAND Gate</h2>
   <p>The NAND gate outputs false (0) only when both of its inputs are true. It is the inverse of the AND gate.</p>
   <table>
      <thead>
         <tr>
            <th>A</th>
            <th>B</th>
            <th>OUTPUT</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>0</td>
            <td>0</td>
            <td>1</td>
         </tr>
         <tr>
            <td>0</td>
            <td>1</td>
            <td>1</td>
         </tr>
         <tr>
            <td>1</td>
            <td>0</td>
            <td>1</td>
         </tr>
         <tr>
            <td>1</td>
            <td>1</td>
            <td>0</td>
         </tr>
      </tbody>
   </table>
   <br>
   <h2 class="h2">OR Gate</h2>
   <p>The OR gate outputs true (1) whenever at least one of its inputs is true. </p>
   <table>
      <thead>
         <tr>
            <th>A</th>
            <th>B</th>
            <th>OUTPUT</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>0</td>
            <td>0</td>
            <td>0</td>
         </tr>
         <tr>
            <td>0</td>
            <td>1</td>
            <td>1</td>
         </tr>
         <tr>
            <td>1</td>
            <td>0</td>
            <td>1</td>
         </tr>
         <tr>
            <td>1</td>
            <td>1</td>
            <td>1</td>
         </tr>
      </tbody>
   </table>
   <br>
   <h2 class="h2">NOR Gate</h2>
   <p>The NOR gate outputs true (1) only when both of its inputs are false (0). It is the inverse of the OR gate.</p>
   <table>
      <thead>
         <tr>
            <th>A</th>
            <th>B</th>
            <th>OUTPUT</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>0</td>
            <td>0</td>
            <td>1</td>
         </tr>
         <tr>
            <td>0</td>
            <td>1</td>
            <td>0</td>
         </tr>
         <tr>
            <td>1</td>
            <td>0</td>
            <td>0</td>
         </tr>
         <tr>
            <td>1</td>
            <td>1</td>
            <td>0</td>
         </tr>
      </tbody>
   </table>
   <br>
   <h2 class="h2">XOR Gate</h2>
   <p>The XOR (exclusive OR) gate outputs true (1) only when its inputs are different.</p>
   <table>
      <thead>
         <tr>
            <th>A</th>
            <th>B</th>
            <th>OUTPUT</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>0</td>
            <td>0</td>
            <td>0</td>
         </tr>
         <tr>
            <td>0</td>
            <td>1</td>
            <td>1</td>
         </tr>
         <tr>
            <td>1</td>
            <td>0</td>
            <td>1</td>
         </tr>
         <tr>
            <td>1</td>
            <td>1</td>
            <td>0</td>
         </tr>
      </tbody>
   </table>
   <br><br>
   <h1 class="h1">SHDL (Simple Hardware Description Language) Documentation</h1>
    <p>SHDL is designed for educational purposes to demystify the principles of digital logic and circuit design through programming. It enables users to define, simulate, and explore digital circuits programmatically.</p>
    
    <h2 class="h2">Language Structure</h2>
    <p>An SHDL program comprises variable declarations, gate definitions, and gate instantiations to form a digital circuit. It supports basic logic operations such as AND, OR, NOT, and XOR.</p>

    <h2 class="h2">Variables</h2>
    <p>Variables in SHDL are categorized into Inputs, Outputs, and Wires.</p>

    <h2 class="h2">Gates</h2>
    <p>Gates are user-defined entities encapsulating specific logical functionalities. Gates cannot be nested or invoke themselves recursively.</p>

    <h2 class="h2">Syntax Highlights</h2>
    <h3 class="h3">Variable Declaration</h3>
    <pre>
   INPUT &lt;variable_name&gt;
   OUTPUT &lt;variable_name&gt;
   WIRE &lt;variable_name&gt;
    </pre>

    <h3 class="h3">Gate Definition and Constraints</h3>
    <pre>
STARTGATE &lt;gate_name&gt; INPUT &lt;input1&gt; [INPUT &lt;input2&gt; ...] OUTPUT &lt;output1&gt; [OUTPUT &lt;output2&gt; ...]
    // Operations here
ENDGATE
    </pre>

    <h3 class="h3">Operations</h3>
    <pre>
AND, OR, NOT, XOR
    </pre>
    <br>
    <h2 class="h2">Example</h2>
    <pre>
INPUT A
INPUT B
OUTPUT S
OUTPUT C
WIRE T1
WIRE T2

STARTGATE MYXOR INPUT X INPUT Y OUTPUT Z
    OR X Y T1
    AND X Y T2
    NOT T2 T3
    AND T1 T3 Z
ENDGATE

STARTGATE ADDER INPUT X INPUT Y OUTPUT Z OUTPUT I    
    MYXOR X Y Z
    AND X Y I
ENDGATE

ADDER A B S C
    </pre>
    <br>
    <h2 class="h2">Conclusion</h2>
    <p>SHDL simplifies the exploration of digital logic and circuit design principles, serving as an invaluable tool for educational contexts.</p>

</main>