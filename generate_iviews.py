# --- Portal iView XML Creation Python Script - Automate iView (url) Creation -------
# --- Check comments beside each line to modify file name/path name, details  -------
# --- Multiple iViews can be created in Seconds saving lot of efforts         -------
# --- Created, Modified, Maintained by Avik Roy Barman                        -------
import pandas as pd
import sys
from xml.sax.saxutils import escape

# --- CONFIGURATION ---
EXCEL_FILE = 'PortalXMLExample.xlsx' # change the name of the file in the same folder (with ID, Title, URL)
OUTPUT_XML = 'portal_upload.xml' #Output xml file which has to be uploaded
# Note: Use the path without 'pcd:' prefix if using the format provided
TARGET_PCD_PARENT = 'portal_content/' #Change path where you want the iViews to be created

def generate_sap_xml(excel_path, output_path):
    try:
        # Load Excel - Ensure columns are 'ID', 'Title', and 'URL'
        df = pd.read_excel(excel_path)
    except Exception as e:
        print(f"ERROR: Could not read Excel file. Details: {e}")
        sys.exit(1)

    # Header using GenericCreator syntax
    xml_header = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<GenericCreator author="SAP" version="Portal 1.0" mode="execute" '
        'report.level="debug" default.locale="en" createMode="1" ignore="false">\n\n'
    )
    xml_footer = '</GenericCreator>'
    
    items_xml = ""
    
    for index, row in df.iterrows():
        # Escape special characters for XML safety
        clean_url = escape(str(row['URL']))
        clean_title = escape(str(row['Title']))
        clean_id = str(row['ID']).replace(" ", "_")
        
        # Construct the Context block based on your template
        item = f"""    <Context parent="{TARGET_PCD_PARENT}" name="{clean_id}" 
             objectClass="com.sapportals.portal.iview" 
             template="par:/applications/com.sap.portal.httpconnectivity.urliviews/components/runtime" 
             title="{clean_title}"
             create_as="0">
        
        <Attributes>
            <Attribute name="url" type="string">
                <AttributeValue value="{clean_url}"/>
            </Attribute>
            <Attribute name="com.sap.portal.navigation.ShowType" type="string">
                <AttributeValue value="1"/> </Attribute>
            <Attribute name="com.sap.portal.iview.HeightType" type="string" isOrdered="true">
                <AttributeValue value="FULL_PAGE"/>
            </Attribute>
            <Attribute name="ShowBorder" type="string">
                <AttributeValue value="true"/>
            </Attribute>
            <Attribute name="ForcedExternalWindow" type="string">
                <AttributeValue value="true"/>
            </Attribute>
            <Attribute name="EnableActivityReporting" type="string">
                <AttributeValue value="true"/>
            </Attribute>
        </Attributes>
    </Context>\n\n"""
        items_xml += item

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(xml_header + items_xml + xml_footer)
    
    print(f"File generated: {output_path}")
    print(f"Processed {len(df)} URLs successfully.")

if __name__ == "__main__":
    generate_sap_xml(EXCEL_FILE, OUTPUT_XML)
