<?xml version="1.0"?>
<document filename="Account_Move.pdf">
    <template pageSize="(369.0,290.0)" title="Account Move" author="Jeff Wang" allowSplitting="20">
        <pageTemplate id="first">
            <frame id="first" x1="10.0" y1="1.0" height="280" width="341"/>
        </pageTemplate>
    </template>
    <stylesheet>
<!-- 不需要这么多style吧 ？ -->
        <blockTableStyle id="Standard_Outline">
            <blockAlignment value="LEFT"/>
            <blockValign value="TOP"/>
        </blockTableStyle>
        <blockTableStyle id="&#x8868;&#x683C;6">
            <blockAlignment value="LEFT"/>
            <blockValign value="TOP"/>
        </blockTableStyle>
        <blockTableStyle id="&#x8868;&#x683C;1">
            <blockAlignment value="LEFT"/>
            <blockValign value="TOP"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="0,0" stop="0,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="0,0" stop="0,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="1,0" stop="1,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="1,0" stop="1,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="2,0" stop="2,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="2,0" stop="2,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="3,0" stop="3,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="3,0" stop="3,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="4,0" stop="4,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="4,0" stop="4,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="5,0" stop="5,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="5,0" stop="5,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="5,-1" stop="5,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="6,0" stop="6,-1"/>
            <lineStyle kind="LINEAFTER" colorName="#008000" thickness="0.2"  start="6,0" stop="6,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="6,0" stop="6,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="6,-1" stop="6,-1"/>
        </blockTableStyle>
        <blockTableStyle id="&#x8868;&#x683C;2">
            <blockAlignment value="LEFT"/>
            <!--<blockValign value="Top"/>-->
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="0,0" stop="0,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="0,-1" stop="0,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="1,0" stop="1,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="1,-1" stop="1,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="2,0" stop="2,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="2,0" stop="2,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="2,-1" stop="2,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="3,0" stop="3,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="3,0" stop="3,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="3,-1" stop="3,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="4,0" stop="4,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="4,0" stop="4,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="4,-1" stop="4,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="5,0" stop="5,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="5,-1" stop="5,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="6,0" stop="6,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="6,-1" stop="6,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="7,0" stop="7,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="7,-1" stop="7,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="8,0" stop="8,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="8,-1" stop="8,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="9,0" stop="9,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="9,-1" stop="9,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="10,0" stop="10,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="10,-1" stop="10,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="11,0" stop="11,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="11,-1" stop="11,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="12,0" stop="12,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="12,-1" stop="12,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="13,0" stop="13,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="13,-1" stop="13,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="14,0" stop="14,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="14,-1" stop="14,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="15,0" stop="15,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2" start="15,-1" stop="15,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="16,0" stop="16,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="16,-1" stop="16,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="17,0" stop="17,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="17,-1" stop="17,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="18,0" stop="18,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="18,-1" stop="18,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="19,0" stop="19,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="19,-1" stop="19,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="20,0" stop="20,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="20,-1" stop="20,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="21,0" stop="21,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="21,-1" stop="21,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="22,0" stop="22,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="22,-1" stop="22,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="23,0" stop="23,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="23,-1" stop="23,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="24,0" stop="24,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="24,-1" stop="24,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="25,0" stop="25,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="25,-1" stop="25,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="26,0" stop="26,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="26,-1" stop="26,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="27,0" stop="27,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="27,-1" stop="27,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="28,0" stop="28,-1"/>
            <lineStyle kind="LINEAFTER" colorName="#008000" thickness="0.2"  start="28,0" stop="28,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="28,-1" stop="28,-1"/>
        </blockTableStyle>
        <blockTableStyle id="&#x8868;&#x683C;3">
            <blockAlignment value="LEFT"/>
            <blockValign value="TOP"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="0,0" stop="10,10"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="0,0" stop="0,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="1,0" stop="1,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="1,0" stop="1,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="2,0" stop="2,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="2,0" stop="2,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="3,0" stop="3,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="3,0" stop="3,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="4,0" stop="4,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="4,0" stop="4,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="5,0" stop="5,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="5,0" stop="5,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="6,0" stop="6,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="6,0" stop="6,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="7,0" stop="7,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="7,0" stop="7,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="8,0" stop="8,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="8,0" stop="8,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="9,0" stop="9,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="9,0" stop="9,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="10,0" stop="10,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="10,0" stop="10,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="11,0" stop="11,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="11,0" stop="11,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="12,0" stop="12,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="12,0" stop="12,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="13,0" stop="13,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="13,0" stop="13,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="14,0" stop="14,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="14,0" stop="14,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#ff0000" thickness="0.2" start="15,0" stop="15,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="15,0" stop="15,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="16,0" stop="16,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="16,0" stop="16,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="17,0" stop="17,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="17,0" stop="17,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="18,0" stop="18,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="18,0" stop="18,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="19,0" stop="19,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="19,0" stop="19,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="20,0" stop="20,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="20,0" stop="20,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="21,0" stop="21,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="21,0" stop="21,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="22,0" stop="22,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="22,0" stop="22,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="23,0" stop="23,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="23,0" stop="23,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="24,0" stop="24,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="24,0" stop="24,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="25,0" stop="25,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="25,0" stop="25,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="26,0" stop="26,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="26,0" stop="26,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#ff0000" thickness="0.2" start="27,0" stop="27,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="27,0" stop="27,0"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="28,0" stop="28,-1"/>
            <lineStyle kind="LINEAFTER" colorName="#008000" thickness="0.2"  start="28,0" stop="28,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="28,0" stop="28,0"/>
        </blockTableStyle>
        <blockTableStyle id="&#x8868;&#x683C;4">
            <blockAlignment value="LEFT"/>
            <blockValign value="TOP"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="0,0" stop="0,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="0,-1" stop="0,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="1,0" stop="1,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="1,-1" stop="1,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="2,0" stop="2,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="2,0" stop="2,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="2,-1" stop="2,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="3,0" stop="3,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="3,0" stop="3,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="3,-1" stop="3,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="4,0" stop="4,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="4,0" stop="4,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="4,-1" stop="4,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="5,0" stop="5,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="5,-1" stop="5,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="6,0" stop="6,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="6,-1" stop="6,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="7,0" stop="7,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="7,-1" stop="7,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="8,0" stop="8,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="8,-1" stop="8,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="9,0" stop="9,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="9,-1" stop="9,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="10,0" stop="10,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="10,-1" stop="10,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="11,0" stop="11,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="11,-1" stop="11,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="12,0" stop="12,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="12,-1" stop="12,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="13,0" stop="13,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="13,-1" stop="13,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="14,0" stop="14,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="14,-1" stop="14,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#ff0000" thickness="0.2" start="15,0" stop="15,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="15,-1" stop="15,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="16,0" stop="16,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="16,-1" stop="16,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="17,0" stop="17,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="17,-1" stop="17,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="18,0" stop="18,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="18,-1" stop="18,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="19,0" stop="19,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="19,-1" stop="19,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="20,0" stop="20,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="20,-1" stop="20,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="21,0" stop="21,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="21,-1" stop="21,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="22,0" stop="22,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="22,-1" stop="22,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="23,0" stop="23,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="23,-1" stop="23,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="24,0" stop="24,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="24,-1" stop="24,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="25,0" stop="25,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="25,-1" stop="25,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="26,0" stop="26,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="26,-1" stop="26,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#ff0000" thickness="0.2" start="27,0" stop="27,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="27,-1" stop="27,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="28,0" stop="28,-1"/>
            <lineStyle kind="LINEAFTER" colorName="#008000" thickness="0.2"  start="28,0" stop="28,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="28,-1" stop="28,-1"/>
        </blockTableStyle>
        <blockTableStyle id="tablefoot">
            <blockAlignment value="LEFT"/>
            <blockValign value="TOP"/>
        </blockTableStyle>
        <blockTableStyle id="&#x8868;&#x683C;5">
            <blockAlignment value="LEFT"/>
            <blockValign value="TOP"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="0,0" stop="0,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="0,0" stop="0,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="0,-1" stop="0,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="1,0" stop="1,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="1,0" stop="1,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="1,-1" stop="1,-1"/>
            <lineStyle kind="LINEBEFORE" colorName="#008000" thickness="0.2"  start="2,0" stop="2,-1"/>
            <lineStyle kind="LINEAFTER" colorName="#008000" thickness="0.2"  start="2,0" stop="2,-1"/>
            <lineStyle kind="LINEABOVE" colorName="#008000" thickness="0.2"  start="2,0" stop="2,0"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="2,-1" stop="2,-1"/>
            <lineStyle kind="LINEAFTER" colorName="#008000" thickness="0.2"  start="3,0" stop="3,-1"/>
            <lineStyle kind="LINEBELOW" colorName="#008000" thickness="0.2"  start="3,-1" stop="3,-1"/>
        </blockTableStyle>
        <initialize>
            <paraStyle name="all" alignment="justify"/>
        </initialize>
        <paraStyle name="P1" fontName="Helvetica" fontSize="6.0" leading="8" alignment="CENTER"/>
        <paraStyle name="P2" fontName="Helvetica" fontSize="2.0" leading="3"/>
        <paraStyle name="P3" fontName="Helvetica" fontSize="5.0" leading="7" alignment="CENTER"/>
        <paraStyle name="P4" fontName="Helvetica" fontSize="8.0" leading="10" alignment="CENTER"/>
        -->
        <paraStyle name="P5" fontName="Helvetica" fontSize="2.0" leading="3"/>
        <paraStyle name="P6" fontName="Helvetica" fontSize="2.0" leading="3"/>
        <paraStyle name="P7" fontName="Helvetica" fontSize="6.0" leading="8" alignment="CENTER"/>
        <paraStyle name="P8" fontName="Helvetica" fontSize="7.0" leading="8" alignment="JUSTIFY"/>
        <paraStyle name="P9" fontName="Helvetica" fontSize="7.0" leading="8" alignment="RIGHT"/>
        <paraStyle name="P10" fontName="Helvetica" fontSize="5.0" leading="7" alignment="CENTER"/>
        <paraStyle name="P11" fontName="Helvetica" fontSize="9.0" leading="14" alignment="CENTER"/>
        <paraStyle name="P12" fontName="Helvetica" fontSize="7.0" leading="14" alignment="LEFT"/>
        <paraStyle name="P13" fontName="Helvetica" fontSize="7.0" leading="14" alignment="RIGHT"/>
        <paraStyle name="P14" fontName="Helvetica" fontSize="6.0" leading="14" alignment="LEFT"/>
        <paraStyle name="P15" fontName="Helvetica" fontSize="5.0" leading="14" alignment="LEFT"/>
        <paraStyle name="Standard" fontName="Helvetica"/>
        <paraStyle name="Heading" fontName="Helvetica" fontSize="14.0" leading="17" spaceBefore="12.0" spaceAfter="6.0"/>
        <paraStyle name="Text body" fontName="Helvetica" spaceBefore="0.0" spaceAfter="6.0"/>
        <paraStyle name="List" fontName="Helvetica" spaceBefore="0.0" spaceAfter="6.0"/>
        <paraStyle name="Caption" fontName="Helvetica" fontSize="12.0" leading="15" spaceBefore="6.0" spaceAfter="6.0"/>
        <paraStyle name="Index" fontName="Helvetica"/>
        <paraStyle name="Table Contents" fontName="Helvetica"/>
        <paraStyle name="Table Heading" fontName="Helvetica" alignment="CENTER"/>
        <images/>
    </stylesheet>
    <story>
        <section>
            <para style="P2">[[repeatIn(objects,'move')]]</para>
            <section>
                <para style="P2">[[repeatIn(range(paginate(move.line_id,5)),'page')]]</para>
                <para style="P11">记账凭证</para>
                <para style="P10">[[move.date]]</para>
                <blockTable colWidths="200,100,41" style="&#x8868;&#x683C;6">
                    <tr>
                        <td>
                            <para style="P8">公司名称:[[move.company_id.name]]</para>
                        </td>
                        <td>
                            <para style="P8">凭证号: [[move.name]]</para>
                        </td>
                        <td>
                            <para style="P9">[[page+1]]/[[paginate(move.line_id,5)]]</para>
                        </td>
                    </tr>
                    </blockTable>
                <para style="P8"/>
                <blockTable colWidths="40,44,24,24,42,84,84" style="&#x8868;&#x683C;1">
                    <tr>
                        <td>
                            <para style="P1">摘要</para>
                        </td>
                        <td>
                            <para style="P1">会计科目</para>
                        </td>
                        <td>
                            <para style="P1">币别</para>
                        </td>
                        <td>
                            <para style="P1">汇率</para>
                        </td>
                        <td>
                            <para style="P1">原始金额</para>
                        </td>
                        <td>
                            <para style="P1">借方</para>
                        </td>
                        <td>
                            <para style="P1">贷方</para>
                        </td>
                    </tr>
                    </blockTable>
                <blockTable colWidths="40,44,24,24,42,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0" style="&#x8868;&#x683C;2" rowHeights="0.5cm">
                    <tr>
                        <td>
                            <para style="P1">
                                <font color="white"></font>
                            </para>
                        </td>
                        <td>
                            <para style="P1">
                                <font color="white"></font>
                            </para>
                        </td>
                        <td>
                            <para style="P1">单位</para>
                        </td>
                        <td>
                            <para style="P1">单价</para>
                        </td>
                        <td>
                            <para style="P1">数量</para>
                        </td>
                        <td>
                            <para style="P1">十</para>
                        </td>
                        <td>
                            <para style="P1">亿</para>
                        </td>
                        <td>
                            <para style="P1">千</para>
                        </td>
                        <td>
                            <para style="P1">佰</para>
                        </td>
                        <td>
                            <para style="P1">十</para>
                        </td>
                        <td>
                            <para style="P1">万</para>
                        </td>
                        <td>
                            <para style="P1">千</para>
                        </td>
                        <td>
                            <para style="P1">佰</para>
                        </td>
                        <td>
                            <para style="P1">十</para>
                        </td>
                        <td>
                            <para style="P1">元</para>
                        </td>
                        <td>
                            <para style="P1">角</para>
                        </td>
                        <td>
                            <para style="P1">分</para>
                        </td>
                        <td>
                            <para style="P1">十</para>
                        </td>
                        <td>
                            <para style="P1">亿</para>
                        </td>
                        <td>
                            <para style="P1">千</para>
                        </td>
                        <td>
                            <para style="P1">佰</para>
                        </td>
                        <td>
                            <para style="P1">十</para>
                        </td>
                        <td>
                            <para style="P1">万</para>
                        </td>
                        <td>
                            <para style="P1">千</para>
                        </td>
                        <td>
                            <para style="P1">佰</para>
                        </td>
                        <td>
                            <para style="P1">十</para>
                        </td>
                        <td>
                            <para style="P1">元</para>
                        </td>
                        <td>
                            <para style="P1">角</para>
                        </td>
                        <td>
                            <para style="P1">分</para>
                        </td>
                    </tr>
                    </blockTable>
                <section>
                    <para style="P2">[[repeatIn(move.line_id[page*5:page*5+5],'line')]]</para>
                    <blockTable colWidths="40,44,24,24,42,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0" rowHeights="0.50cm" style="&#x8868;&#x683C;3">
                        <tr>
                            <td>
                                <para style="P3">[[line.name]]</para>
                            </td>
                            <td>
                                <para style="P3">[[account_name(line.account_id.id)]] [[line.product_id.name or (account_partner(line.account_id.id, line.partner_id.name) or '')]]</para>
                            </td>
                            <td>
                                <para style="P6">[[exchange_rate(line) and line.currency_id.name or '']]</para>
                            </td>
                            <td>
                                <para style="P6">[[formatLang(exchange_rate(line) or '')]]</para>
                            </td>
                            <td>
                                <para style="P6">[[formatLang(line.amount_currency or '')]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[0] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[1] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[2] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[3] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[4] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[5] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[6] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[7] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[8] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[9] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[10] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.debit)[11] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[0] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[1] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[2] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[3] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[4] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[5] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[6] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[7] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[8] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[9] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[10] ]]</para>
                            </td>
                            <td>
                                <para style="P4">[[rmb_format(line.credit)[11] ]]</para>
                            </td>

                        </tr>
                    </blockTable>
                    <blockTable colWidths="40,44,24,24,42,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0" rowHeights="0.50cm" style="&#x8868;&#x683C;4">
                        <tr>
                            <td>
                                <para style="P3"></para>
                            </td>
                            <td>
                                <para style="P3"></para>
                            </td>
                            <td>
                                <para style="P3">[[line.product_uom_id.name or '']]</para>
                            </td>
                            <td>
                                <para style="P3">[[formatLang(line.product_uom_id and unit_price(line) or '')]]</para>
                            </td>
                            <td>
                                <para style="P3">[[line.product_uom_id and line.quantity or '' ]]</para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                        </tr>
                    </blockTable>
                </section>
                <section>
                    <para style="P2">[[repeatIn(range(5-len(move.line_id[page*5:page*5+5])),'bl')]]</para>
                    <!--<blockTable colWidths="40,42,24,24,44,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0" rowHeights="0.50cm"  style="&#x8868;&#x683C;3">
                        <tr>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6"></para>
                            </td>
                            <td>
                                <para style="P6"></para>
                            </td>
                            <td>
                                <para style="P6"></para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                            <td>
                                <para style="P6">
                                    <font color="white"></font>
                                </para>
                            </td>
                        </tr>
                    </blockTable>
		    <blockTable colWidths="40,42,24,24,44,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0" rowHeights="0.50cm"  style="&#x8868;&#x683C;4">
                        <tr>
                            <td>
                                <para style="P3"></para>
                            </td>
                            <td>
                                <para style="P3"></para>
                            </td>
                            <td>
                                <para style="P3"></para>
                            </td>
                            <td>
                                <para style="P3"></para>
                            </td>
                            <td>
                                <para style="P3"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                            <td>
                                <para style="P4"></para>
                            </td>
                        </tr>
			</blockTable>-->
                </section>
                <blockTable colWidths="40,134,84,84" style="&#x8868;&#x683C;5" rowHeights="0.50cm">
                    <tr>
                        <td>
                            <para style="P15">附件：[[move.proof or '0' ]] 张</para>
                        </td>
                        <td>
                            <para style="P12">合计：（大写）[[rmb_upper(move.amount)]]</para>
                        </td>
                        <td>
                            <para style="P13">[[move.company_id.currency_id.symbol]][[move.amount]]</para>
                        </td>
                        <td>
                            <para style="P13">[[move.company_id.currency_id.symbol]][[move.amount]]</para>
                        </td>
                    </tr>
                </blockTable>
                <blockTable colWidths="68,68,68,68,68" style="tablefoot" rowHeights="1.5cm">
                    <tr>
                        <td>
                            <para style="P14">核准：</para>
                        </td>
                        <td>
                            <para style="P14">过帐：</para>
                        </td>
                        <td>
                            <para style="P14">出纳：</para>
                        </td>
                        <td>
                            <para style="P14">制单：[[move.create_uid.name]]</para>
                        </td>
                        <td>
                            <para style="P14">审核：[[move.write_uid.name]]</para>
                        </td>
                    </tr>
                    </blockTable>
                <!-- [<pageBreak>[[ paginate(move.line_id,5) == page+1  and removeParentNode('pageBreak')]]</pageBreak>] -->
                <para style="P6">
                    <font color="white"></font>
                </para>
            </section>
        </section>
    </story>
</document>

