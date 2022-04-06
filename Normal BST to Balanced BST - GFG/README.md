# Normal BST to Balanced BST
## Easy 
<div class="problem-statement">
                <p><a onclick="gtagHelperFunction('clickopen','salesevent_gsc_problemspage_promobanner')" href="https://practice.geeksforgeeks.org/summer-carnival-2022?utm_source=practiceproblems&amp;utm_medium=problemspromobanner&amp;utm_campaign=gsc22" target="_blank"></a></p><div style="margin: 14px 0px !important;" class="row"><a onclick="gtagHelperFunction('clickopen','salesevent_gsc_problemspage_promobanner')" href="https://practice.geeksforgeeks.org/summer-carnival-2022?utm_source=practiceproblems&amp;utm_medium=problemspromobanner&amp;utm_campaign=gsc22" target="_blank">             <div class="col-md-12" style="cursor:pointer;background: #EFF8F3 0% 0% no-repeat padding-box; display: flex; align-items: center; position:                 relative; padding: 1.5%; border-radius: 10px; display: inline-block; text-align: center; font-weight: 600; color: #333"> <img src="https://media.geeksforgeeks.org/img-practice/gcs2022thumbnail-1649059370.png" alt="Lamp" width="46" height="40" style="background: transparent 0% 0% no-repeat padding-box;opacity: 1; margin: 0 16px;" class="img-responsive"> Geeks Summer Carnival is LIVE NOW &nbsp; <i class="fa fa-external-link" aria-hidden="true"></i> </div></a></div><p><span style="font-size:20px">Given a&nbsp;Binary&nbsp;Search&nbsp;Tree<strong>,</strong> modify the given BST such that itis balanced and has minimum possible height.</span></p>

<p><span style="font-size:20px">Examples :</span></p>

<pre><span style="font-size:18px">Input:
       30
      /
     20
    /
   10
Output:
     20
   /   \
 10     30

Input:
         4
        /
       3
      /
     2
    /
   1
Output:
      3            3           2
    /  \         /  \        /  \
   1    4   OR  2    4  OR  1    3   OR ..
    \          /                   \
     2        1                     4 
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
The task is to complete the function <strong>buildBalancedTree()</strong> which takes root as the input argument, and returns the root of tree after converting the given BST&nbsp;into a balanced BST that has minimum possible height</span><span style="font-size:20px">.</span><span style="font-size:18px"> The driver code will print the height of the updated tree in output itself. </span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N)<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(N)<br>
Here N denotes total number of nodes in given BST.</span></p>

<p><br>
<span style="font-size:20px"><strong>Constraints:</strong><br>
1&lt;=N&lt;=200</span></p>
 <p></p>
            </div>