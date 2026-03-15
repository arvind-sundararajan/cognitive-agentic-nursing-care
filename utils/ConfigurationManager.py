```json
{
    "utils/ConfigurationManager.py": {
        "content": "
import logging
from typing import Dict, Any
from SemanticKernel import StateGraph
from Letta import MemoryManager
from AgentOps import Agent

class ConfigurationManager:
    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Initialize the ConfigurationManager with a given configuration.

        Args:
        - config (Dict[str, Any]): The configuration dictionary.

        Raises:
        - ValueError: If the configuration is invalid.
        """
        try:
            self.config = config
            self.non_stationary_drift_index = config['non_stationary_drift_index']
            self.stochastic_regime_switch = config['stochastic_regime_switch']
            self.memory_manager = MemoryManager()
            self.state_graph = StateGraph()
            self.agent = Agent()
            logging.info('ConfigurationManager initialized successfully.')
        except Exception as e:
            logging.error(f'Error initializing ConfigurationManager: {e}')
            raise ValueError('Invalid configuration')

    def update_config(self, new_config: Dict[str, Any]) -> None:
        """
        Update the configuration with new values.

        Args:
        - new_config (Dict[str, Any]): The new configuration dictionary.

        Raises:
        - ValueError: If the new configuration is invalid.
        """
        try:
            self.config.update(new_config)
            self.non_stationary_drift_index = new_config.get('non_stationary_drift_index', self.non_stationary_drift_index)
            self.stochastic_regime_switch = new_config.get('stochastic_regime_switch', self.stochastic_regime_switch)
            logging.info('Configuration updated successfully.')
        except Exception as e:
            logging.error(f'Error updating configuration: {e}')
            raise ValueError('Invalid new configuration')

    def get_config(self) -> Dict[str, Any]:
        """
        Get the current configuration.

        Returns:
        - Dict[str, Any]: The current configuration dictionary.
        """
        try:
            return self.config
        except Exception as e:
            logging.error(f'Error getting configuration: {e}')
            raise ValueError('Failed to get configuration')

    def simulate_rocket_science(self) -> None:
        """
        Simulate the 'Rocket Science' problem using the current configuration.

        Raises:
        - ValueError: If the simulation fails.
        """
        try:
            self.agent.run_simulation(self.state_graph, self.memory_manager, self.non_stationary_drift_index, self.stochastic_regime_switch)
            logging.info('Rocket Science simulation completed successfully.')
        except Exception as e:
            logging.error(f'Error simulating Rocket Science: {e}')
            raise ValueError('Simulation failed')

if __name__ == '__main__':
    config = {
        'non_stationary_drift_index': 0.5,
        'stochastic_regime_switch': True
    }
    manager = ConfigurationManager(config)
    manager.simulate_rocket_science()
",
        "commit_message": "feat: implement specialized ConfigurationManager logic"
    }
}
```