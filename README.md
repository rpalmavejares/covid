# Custom scheme converter #

This software allow you to convert the original V3 files of the artic protocol for the sequencing and assembly of covid-19 samples described in https://artic.network/ncov-2019 to a custom set of files suited for specific primer pairs selected in your nanopone sequencing pipeline.

### **Important Info** ###

Your original artic files should be on a directory similar to :

        artic-ncov2019/primer_schemes/nCoV-2019/V1
        artic-ncov2019/primer_schemes/nCoV-2019/V2
        artic-ncov2019/primer_schemes/nCoV-2019/V3
**The distribution of all primers along the genome can be found on the https://github.com/rpalmavejares/covid/blob/master/nCoV-2019.pdf file**

## USAGE ## 

### This script uses python 3.7 ###

        python scheme_converter.py custom_primers_pairs_file

Your "custom_primers_pairs_file" should be a TAB separated file with the list or primers selected in the sequencing step.

### Example of custom_primers_pairs_file ###

\* If your primer probe lenght is 400pb-450pb, your **custom_primers_pairs_file** probes should be in order, exactly as it follows.

        nCoV-2019_1_LEFT    nCoV-2019_1_RIGHT
        nCoV-2019_2_LEFT    nCoV-2019_2_RIGHT
        ...
        ...
        nCoV-2019_98_LEFT   nCoV-2019_98_RIGHT

### However, if you want to amplify 700pb-750pb probes you need to skip the next reverse primer to generate another pair ###

        nCoV-2019_1_LEFT    nCoV-2019_2_RIGHT
        nCoV-2019_2_LEFT    nCoV-2019_4_RIGHT
        nCoV-2019_4_LEFT    nCoV-2019_6_RIGHT
        ...
        and so on ...

*Notice how in this example, we skip nCoV-2019_1_RIGHT, on the first pair .

### The logic for larger primer pairs is is still the same as the previous example. Wanna try to amplify 1050pb probes? same basics, just select 1050pb primer pairs ###

        nCoV-2019_1_LEFT    nCoV-2019_4_RIGHT
        nCoV-2019_4_LEFT    nCoV-2019_7_RIGHT
        nCoV-2019_7_LEFT    nCoV-2019_10_RIGHT
        ...

### What about 1650pb probes?? ###

        nCoV-2019_1_LEFT    nCoV-2019_5_RIGHT
        nCoV-2019_5_LEFT    nCoV-2019_9_RIGHT
        nCoV-2019_9_LEFT    nCoV-2019_13_RIGHT
        ...
## After the execution of the script, 3 new files will be generated for the new primer scheme. Use those to execute the Artic-Minion protocol ##


