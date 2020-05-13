<h2> Custom scheme converter </h2>

This software allow you to convert the original V3 files of the artic protocol for the sequencing and assembly of covid-19 samples described in https://artic.network/ncov-2019 to a custom set of files suited for specific primer pairs selected in your nanopone sequencing pipeline.

<b> ** Important Info ** </b>
<br>
Your original artic files should be on a directory similar to :

artic-ncov2019/primer_schemes/nCoV-2019/V1
<br>
artic-ncov2019/primer_schemes/nCoV-2019/V2
<br>
artic-ncov2019/primer_schemes/nCoV-2019/V3

<h2> USAGE </h2>

This script uses python 3.7 
<br>
<b> python scheme_converter.py custom_primers_pairs_file </b>

<br>

Your "custom_primers_pairs_file" should be a TAB separated file with the list or primers selected in the sequencing step.

<h3> Example of custom_primers_pairs_file </h3>

<h4> If your primer probe lenght is 400pb, your file should look like the original V3 files: </h4>

nCoV-2019_1_LEFT <b> [TAB] </b> nCoV-2019_1_RIGHT<br>
nCoV-2019_2_LEFT <b> [TAB] </b> nCoV-2019_2_RIGHT<br>
...<br>
...<br>
nCoV-2019_98_LEFT <b> [TAB] </b> nCoV-2019_98_RIGHT<br>
<br>
<h4> However, if you want to amplify 800pb probes, you might select 800pb primer pairs, like. </h4> <br>

nCoV-2019_1_LEFT <b> [TAB] </b> nCoV-2019_3_RIGHT<br>
nCoV-2019_3_LEFT <b> [TAB] </b> nCoV-2019_5_RIGHT<br>
nCoV-2019_5_LEFT <b> [TAB] </b> nCoV-2019_7_RIGHT<br>
...<br>

and so on ...<br>

<h4> Wanna try to amplify 1200pb probes? same basics, just select 1200pb primer pairs </h4> 
<br>
nCoV-2019_1_LEFT <b> [TAB] </b> nCoV-2019_4_RIGHT<br>
nCoV-2019_4_LEFT <b> [TAB] </b> nCoV-2019_7_RIGHT<br>
nCoV-2019_7_LEFT <b> [TAB] </b> nCoV-2019_10_RIGHT<br>
...<br>

<h4> What about 1600pb probes?? </h4> <br>
<br>
nCoV-2019_1_LEFT <b> [TAB] </b> nCoV-2019_5_RIGHT<br>
nCoV-2019_5_LEFT <b> [TAB] </b> nCoV-2019_9_RIGHT<br>
nCoV-2019_9_LEFT <b> [TAB] </b> nCoV-2019_13_RIGHT<br>
...<br>

<h4> Wanna push the limits? maybe 30.000pb probes? </h4> 

nCoV-2019_1_LEFT <b> [TAB] </b> nCoV-2019_98_RIGHT<br>

<h4> This probably won't work.... but in case it does, the script got you cover... you madlad. </h4>

<br>

<b> After the execution of the script, remember to replace your 3 new files, to the older ones and you are ready to go, just make sure to save the old ones just in case </b>


