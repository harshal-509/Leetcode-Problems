# Delete a node from BST
## Medium 
<div class="problem-statement">
                <p><a onclick="gtagHelperFunction('clickopen','salesevent_gsc_problemspage_promobanner')" href="https://practice.geeksforgeeks.org/summer-carnival-2022?utm_source=practiceproblems&amp;utm_medium=problemspromobanner&amp;utm_campaign=gsc22" target="_blank"></a></p><div style="margin: 14px 0px !important;" class="row"><a onclick="gtagHelperFunction('clickopen','salesevent_gsc_problemspage_promobanner')" href="https://practice.geeksforgeeks.org/summer-carnival-2022?utm_source=practiceproblems&amp;utm_medium=problemspromobanner&amp;utm_campaign=gsc22" target="_blank">             <div class="col-md-12" style="cursor:pointer;background: #EFF8F3 0% 0% no-repeat padding-box; display: flex; align-items: center; position:                 relative; padding: 1.5%; border-radius: 10px; display: inline-block; text-align: center; font-weight: 600; color: #333"> <img src="https://media.geeksforgeeks.org/img-practice/gcs2022thumbnail-1649059370.png" alt="Lamp" width="46" height="40" style="background: transparent 0% 0% no-repeat padding-box;opacity: 1; margin: 0 16px;" class="img-responsive"> Geeks Summer Carnival is LIVE NOW &nbsp; <i class="fa fa-external-link" aria-hidden="true"></i> </div></a></div><p><span style="font-size:18px">Given a Binary Search Tree and a node value X. Delete the node with the given value X from the BST. If no node with value x exists, then do not make any change.&nbsp;</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>      2
&nbsp;   /   \
&nbsp;  1     3
X = 12
<strong>Output: </strong>1 2 3<strong>
Explanation: </strong>In the given input there
is no node with value 12 , so the tree
will remain same.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;\
 &nbsp; &nbsp;    &nbsp; &nbsp; &nbsp; 2
 &nbsp; &nbsp;&nbsp; &nbsp;       &nbsp;&nbsp;\
 &nbsp; &nbsp; &nbsp;        &nbsp;  8 
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;/&nbsp; &nbsp; \
 &nbsp; &nbsp; &nbsp; &nbsp;     &nbsp;5&nbsp;  &nbsp;  11
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;/&nbsp; \&nbsp; &nbsp; /  \
 &nbsp; &nbsp; &nbsp;     4 &nbsp; &nbsp;7&nbsp; 9 &nbsp;&nbsp;12
X = 9
<strong>Output: </strong>1 2 4 5 7 8 11 12<strong>
Explanation: </strong>In the given input tree after
deleting 9 will be
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  1
&nbsp; &nbsp; &nbsp; &nbsp;   &nbsp; &nbsp;&nbsp;\
&nbsp; &nbsp;     &nbsp;  &nbsp; &nbsp; 2
&nbsp; &nbsp;&nbsp; &nbsp;        &nbsp; &nbsp;\
&nbsp; &nbsp; &nbsp;        &nbsp;  &nbsp; 8
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp;  &nbsp;/&nbsp;  \
&nbsp; &nbsp; &nbsp; &nbsp;        &nbsp;5&nbsp; &nbsp;  11
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; /&nbsp; \&nbsp; &nbsp; &nbsp;\
&nbsp; &nbsp; &nbsp;         4 &nbsp; &nbsp;7&nbsp; &nbsp;&nbsp;&nbsp;12</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function</span><span style="font-size:18px"> <strong>deleteNode()</strong>&nbsp;which takes two&nbsp;arguments. The first being the root of the tree, and an integer <strong>'X'</strong>&nbsp;denoting the node value to be deleted from the BST. Return the root of the BST after deleting the node with value X. Do not make any update if there's no node with value X present in the BST. </span></p>

<p><span style="font-size:18px"><strong>Note: </strong>The generated output will be&nbsp;the inorder traversal of the modified tree.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(Height of the BST).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(Height of the BST).</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>5</sup></span></p>

<p>&nbsp;</p>
 <p></p>
            </div>