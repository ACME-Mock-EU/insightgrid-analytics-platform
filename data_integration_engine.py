# Data Integration Engine
# Multi-source data connectors, transformation, and federation

import pandas as pd

class DataIntegrationEngine:
    def __init__(self):
        self.primary_sources = ['Salesforce', 'Zendesk', 'Snowflake']
        self.custom_connectors = ['ProductEvents', 'BillingEvents', 'BillingAPI', 'TerritorySvc', 'UsageEvents']
    
    def analyze_connector_usage(self, dashboard_df):
        '''Analyze which connectors are used most'''
        connectors = {}
        
        for idx, row in dashboard_df.iterrows():
            sources = row.get('Data Sources Connected', '')
            if pd.notna(sources):
                source_list = [s.strip() for s in str(sources).split(',')]
                for source in source_list:
                    if source not in connectors:
                        connectors[source] = 0
                    connectors[source] += 1
        
        return connectors
    
    def identify_multi_source_dashboards(self, dashboard_df):
        '''Find dashboards using multiple data sources'''
        multi_source = []
        
        for idx, row in dashboard_df.iterrows():
            sources = row.get('Data Sources Connected', '')
            if pd.notna(sources):
                source_count = len([s.strip() for s in str(sources).split(',')])
                if source_count > 1:
                    multi_source.append({
                        'dashboard': row['Feature Name/Dashboard Type'],
                        'sources': source_count,
                        'department': row['Department']
                    })
        
        return multi_source
    
    def connector_reliability(self, dashboard_df):
        '''Assess connector reliability based on data accuracy'''
        reliability = {}
        
        for idx, row in dashboard_df.iterrows():
            sources = row.get('Data Sources Connected', '')
            accuracy = row.get('Performance Metric', '')
            
            if pd.notna(sources) and 'Accuracy' in str(accuracy):
                for source in str(sources).split(','):
                    source = source.strip()
                    if source not in reliability:
                        reliability[source] = {'accuracies': []}
                    try:
                        acc_value = float(str(accuracy).split()[-1])
                        reliability[source]['accuracies'].append(acc_value)
                    except:
                        pass
        
        # Calculate average accuracy per connector
        for source in reliability:
            accuracies = reliability[source]['accuracies']
            reliability[source]['avg_accuracy'] = round(sum(accuracies) / len(accuracies), 3) if accuracies else 0
        
        return reliability

if __name__ == "__main__":
    engine = DataIntegrationEngine()
    print("Data Integration Engine v1.0 initialized")
    print("Connectors: Salesforce, Zendesk, Snowflake + 5 custom")
