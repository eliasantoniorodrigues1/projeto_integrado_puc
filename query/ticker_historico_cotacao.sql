SELECT 
        ticker
      , DATE(date) date
      , open
      , high
      , low
      , volume
      , adj_close
      , close
 FROM `consultor-investimentos.raw_data.t_historico_cotacoes_ibov`
 WHERE
      ticker = 'ABEV3'