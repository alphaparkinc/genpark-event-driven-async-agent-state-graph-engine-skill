from client import EventDrivenAsyncAgentStateGraphEngineClient

def main():
    client = EventDrivenAsyncAgentStateGraphEngineClient()
    res = client.dispatch_agent_workflow('ComplianceRemediationPipeline', {'audit_id': 'aud_9942'})
    print('Workflow Engine: ' + res['workflow_execution_id'] + ' | ' + res['workflow'])
    print('Events Emitted: ' + str(res['events_emitted_count']) + ' | Cyclic Transitions: ' + str(res['cyclic_state_transitions_completed']))
    print('Checkpoints Persisted: ' + str(res['async_step_checkpoints_persisted']) + ' | Status: ' + str(res['workflow_success']))
    print('Snapshot: ' + res['state_snapshot_url'])

if __name__ == '__main__':
    main()
