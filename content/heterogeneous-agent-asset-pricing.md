Keywords: Asset pricing, Incomplete markets, Heterogeneous agents, Human capital\
JEL codes: E21, E24, E32, E44, G11, G12, J24

# Introduction 

How, if at all, does an inability to insure against idiosyncratic endowment shocks affect aggregate asset prices? The literature on this question gives conflicting answers. A seminal result by states that market incompleteness is irrelevant for risk premia in a broad set of continuous-time settings. At the same time, multiple quantitative models break this result by assuming discrete time and countercyclical idiosyncratic risks.[^3] Some studies have argued, either by example or by intuition, that this timing discrepancy can be reconciled with jumps and recursive preferences.[^4] Surprisingly, though, no study has yet systematically evaluated these theoretical claims and their empirical implications.

Using a comprehensive heterogeneous-agent framework with jumps and recursive preferences, this paper characterizes exactly when incomplete markets do and do not matter for risk premia, equity volatility, and the riskfree rate. The framework admits explicit asset pricing solutions and theorems revealing the necessary and sufficient conditions for incomplete markets to matter for risk premia. Consistent with previous claims, agents demand compensation for countercyclical cross-sectional risk if their preferences are not additively separable. Contrary to previous claims, Poisson jumps have no effect on any of these irrelevance conditions. The intuition still holds: the discrete-time risk premium of still disappears in continuous time.

These irrelevance conditions are restrictive, raising the question of whether market incompleteness could possibly explain the data. I show that it can, if (and only if) one allows for non-additive preferences. Specifically, I solve and calibrate a general-equilibrium model with uninsurable human capital, then test the model with asset pricing data and Social Security Administration income data (Guvenen et al. 2014). Agents can invest freely in a bond, the stock market, and their own inalienable human capital, but cannot trade claims to each other's human capital. The model quantitatively explains a host of asset pricing facts with only two assumptions: non-additive preferences and time-varying risk of an idiosyncratic human-capital disaster. While calibrated to match only the time series of asset prices, the model implies a historical time series of cross-sectional income skewness that accurately matches the data. These results suggest that time-variation in cross-sectional income skewness is an important driver of aggregate asset price dynamics. They also reveal that discrete time is not in fact an essential assumption for incomplete markets to make a difference in the aggregate. This finding complements those of and : under a reasonable calibration, their core idiosyncratic-skewness mechanism is robust to the timing of idiosyncratic risks.

The main specification of the heterogeneous-agent framework features agents with identical isoelastic recursive preferences (Duffie and Epstein 1992). From this framework, I derive a series of comprehensive irrelevance results, the most informative of which is as follows. Stochastic cross-sectional risk has no effect on equity risk premia if and only if (i) all agents have time-additive power or log utility and (ii) cross-sectional risks are uncorrelated with aggregate consumption risks. The first condition operates through a well-understood *price-of-risk* channel. Under non-additive preferences, an investor's marginal value of consumption today depends on utility in the future, so cross-sectional risks are priced. Otherwise, the logic applies. The second condition operates through an *endogenous-equity-risk* channel. Stochastic cross-sectional risk always increases equity-return volatility, and investors are always compensated for this risk if it is correlated with systematic consumption risk. Evidently, whether risks arrive as diffusions or jumps is immaterial.

The finding that Poisson jumps do not affect any of these results may be surprising. Several studies have proposed that, with simultaneous jumps to idiosyncratic risk and aggregate consumption, one can reintroduce the mechanism into continuous time (Martin 2013; Panageas 2020). For this to work, there must be multiple consecutive jumps, first to aggregate consumption and cross-sectional risk, and then to idiosyncratic consumption, all within an infinitesimal time interval. This is not possible with Poisson jumps because each Poisson process can only jump at most once over such an interval, and all must jump at the same time. This is not to say jumps cannot ever matter: to revive the usual discrete-time mechanism, we need a jump process with infinite variation. , for example, achieves this with a variance gamma process. I reconcile these facts, and the broader mathematics behind them, in a detailed discussion.

As stated above, the framework's main specification assumes identical isoelastic preferences. This assumption is at once simple enough to convey the main intuition tractably and broad enough to nest most incomplete-market frameworks in the literature. Table [\[tab:littable\]](#tab:littable) summarizes this nesting. Even so, my main theoretical findings generalize to the case of heterogeneous, non-standard recursive preferences. In this case, identical isoelastic preferences are shown to be a special case for irrelevance, because their homotheticity and isoelasticity eliminate the distribution of consumption shares as a state variable. Non-separability and the covariance of shocks to aggregate consumption and cross-sectional risks continue to be the key irrelevance conditions; jumps remain inconsequential.

[]

-2cm

to .9 & & & & &\
& Discrete & Contin. & & Additive & EZ & Other & Het. & & Gaussian & Jumps & CC\
\
Irrelevance results &\
GS & & & & & & & & & & &\
KL && & & & & & & & & &\
Quantitative models &\
CD, STY & & & & & & & & & & &\
S, CG, AB && & & & & & & & & &\
\
Main framework & & & & & & & & & & &\
Generalized framework & & & & & & & & & & &\
Human-capital model & & & & & & & & & & &\

\

The sources of idiosyncratic risk are widespread; among the most well-documented is uninsurable human capital. In a large cross-section of households, show that the skewness of individuals' income shocks is negative and procyclical. Using cross-sectional regressions with consumption data, finds that involuntary job loss is not fully insured. and propose models in which uninsurable human-capital risk arises endogenously from limited commitment and moral hazard. This moral hazard problem may have substantial implications for macroeconomic aggregates; for human capital includes not only the labor income of workers, but also the private business equity of entrepreneurs.[^5]

It is upon this microfoundation that I build the general-equilibrium model with inalienable human capital described above. To capture these facts, I model human capital as a productive asset in which agents can invest or disinvest, subject to asymmetric adjustment costs. Human capital is also subject to risks, including a time-varying probability of an adverse idiosyncratic jump --- a "personal disaster,\" like persistent unemployment. After frictionless trade in the stock and bond markets, this setting gives rise to equilibrium consumption processes featuring uninsured idiosyncratic risk. Despite depending on only one cross-sectional state variable, the calibrated model captures a host of asset pricing facts, including left-skewed human capital returns; low, stable, and procyclical interest rates; and high, countercyclical equity premia, volatility, and Sharpe ratios.

To my knowledge, my model is the first of its kind to quantitatively explain these facts in continuous time. It is closest to the discrete-time models of and , which also assume non-additive utility. My model sheds light on the mechanisms in these papers. In discrete time, risk premia are driven by two channels: a correlation channel, by which idiosyncratic jump risk rises at the same time equities fall; and a price-of-risk channel, operating through preference non-additivity. A novel result of my paper is that, in continuous time, the correlation channel always disappears, even with jumps. This means that these models can only operate in continuous time through the price-of-risk channel. Nevertheless, I show that this is not a problem: the price-of-risk effect alone is sufficient to explain the data. Another major difference from these models is that, instead of assuming autarkic consumption processes outright, investment opportunities are explicit and agents make endogenous consumption-savings decisions. Lastly, I show that this mechanism does not require a conventional "long-run risk\" model with a high elasticity of intertemporal substitution (EIS) and a very persistent state variable: return dynamics can be explained with an EIS of one, risk aversion of two, and cross-sectional skewness that moves at a business-cycle frequency. Hence, I find that models in the spirit of and are robust to the timing of idiosyncratic risks, to endogenous portfolio choice, and to a broad and sensible parameter space.

The quantitative human-capital model helps to resolve an enduring empirical debate over whether cross-sectional risks in the data can explain asset pricing moments.[^6] Because the model has a direct mapping to cross-sectional income data, its predictions are testable. Using historical U.S. data, I show that the model-implied time-variation in cross-sectional income skewness is consistent with time-variation in skewness in income data (Guvenen et al. 2014) and in multiple asset pricing moments. This is strong evidence in favor of the importance of incomplete markets for aggregate asset prices.

Before proceeding, it is worth elaborating on the meaning of "incomplete markets.\" Generally speaking, there are two kinds of market incompleteness. The first, considered in this paper, is when agents lack a sufficient set of securities to insure against idiosyncratic endowment shocks. The second is when market participants face binding portfolio constraints that prevent them from replicating a complete set of consumption plans.[^7] This is the operative mechanism in intermediary asset pricing (He and Krishnamurthy 2013; Brunnermeier and Sannikov 2014). The present study focuses only on the first category, primarily because it is the kind assumed by the irrelevance results and quantitative models mentioned above.[^8] The inclusion of binding portfolio constraints or dynamic changes in the composition of unconstrained agents --- akin to entry into and exit from the market (Basak and Cuoco 1998; Gârleanu and Panageas 2015) --- will be fruitful extensions of this paper's framework.

The rest of the paper is organized as follows. Section 2 lays out the assumed economic setting, solves for asset prices and returns, and presents and interprets the main theoretical results of the paper. In Section 3, I present and empirically assess the calibrated human-capital model. Section 4 concludes. The Online Appendix contains all proofs.

# The framework and theoretical results 

In this section, I lay out the heterogeneous-agent asset pricing framework with jumps, recursive preferences, and uninsurable idiosyncratic endowment risks. Within this framework, I solve for the prices of, and returns on, a riskfree bond and risky stocks. I then derive from these results the conditions under which incomplete markets matter for asset-price moments.

## The economic setting 

We begin with a description of the individuals populating this economy.

**Assumption 1** (Agents). *There is a unit measure of infinitely lived agents, indexed by $i\in\mathcal{I}=[0,1]$. An agent is defined by a felicity function $\bar{f}^{(i)}$ and an equilibrium consumption process $C_i$, both of which are described below.*

These individuals face uncertainty in the form of systematic and idiosyncratic Brownian and Poisson jump risks. These risks are formalized as follows.

**Assumption 2** (Information). *Uncertainty is represented by the filtered probability space $(\Omega,\mathcal{F},\mathbf{F},\mathbb{P})$. The filtration $\mathbf{F}=\{\mathcal{F}_t:t\geq0\}$ is the augmentation under $\mathbb{P}$ of the filtration generated by $\{B,N,\{B_i,N_i:i\in\mathcal{I}\}\}$, where*

1.  *$B=\left\{\bigl[B_t^{(1)},\dots,B_t^{(m)}\bigr]^\top:t\geq0\right\}$ is an $m$-dimensional Brownian motion,*

2.  *$N=\left\{\bigl[N_t^{(1)},\dots,N_t^{(n)}\bigr]^\top:t\geq0\right\}$ is an $n$-dimensional Poisson process with constant corresponding intensity $\lambda=\bigl[\lambda^{(1)},\dots,\lambda^{(n)}\bigr]^\top$,*

3.  *each $B_i=\{B_{it}:t\geq0\}$ is a one-dimensional Brownian motion, and*

4.  *each $N_i=\{N_{it}:t\geq0\}$ is a one-dimensional Poisson process with corresponding intensity given by the stochastic process $\eta$.[^9]*

*All of these processes are independent of each other.*

Given this information structure, we can define the underlying state variable governing the time-variation in cross-sectional consumption risk. This quantity, denoted by $X$, will determine the cross-sectional moments (variance, skewness, etc.) of idiosyncratic consumption growth. Thus, we can think of $X_t$ as a sufficient statistic for the time-$t$ distribution of idiosyncratic risks. For instance, in the model in Section 3, $X$ represents the time-varying probability of an idiosyncratic human-capital disaster.

**Assumption 3** (Cross-sectional risk). *The stochastic process $X$, which we call *cross-sectional risk*, solves the stochastic differential equation[^10] $$\begin{equation}
dX_t=\mu_X(X_{t})dt+\sigma_X(X_{t})^\top dB_t + \sum_{j=1}^n\zeta_X^{(j)}(X_{t^-})dN_{t}^{(j)}
\label{eq:dcrossrisk_setup}
\end{equation}$$ with initial condition $X_{0}$. The functions $\mu_X$, $\sigma_X$, and $\zeta_{X}^{(j)}$ satisfy the necessary conditions for $X$ to be unique.*

The key assumption here is that cross-sectional risk is stochastic and, in particular, subject to jumps. The presence of multiple jumps with deterministic sizes $\zeta_{Xt}^{(j)}$ is isomorphic to having a single jump with intensity determined by some i.i.d. random variable $Z_X^{(j)}$ with $n$-dimensional support.[^11] Note that the assumption that $X$ is unidimensional is simply made for expositional and analytical simplicity; one can easily extend all of the following results to a multidimensional stochastic process.

We now define the set of consumption processes that hold for each agent in equilibrium --- that is, after they make their consumption and savings decisions.[^12] Let $\mathcal{C}$ represent the set of feasible consumption processes $C$. Then the consumption of each agent $i\in\mathcal{I}$ is a stochastic process $C_i\in\mathcal{C}$, and aggregate consumption, defined by $C_t=\int_\mathcal{I}C_{it}di$, is the total endowment consumed by all agents collectively.[^13] Finally, let $\theta_{it}=C_{it}/C_t$ denote agent $i$'s *consumption share* and $\Theta_t = \{\theta_{it}:i\in\mathcal{I}\}$ the set of all consumption shares.

**Assumption 4** (Equilibrium consumption). *The aggregate consumption process $C\in\mathcal{C}$ is the unique solution to the stochastic differential equation $$\begin{equation}
\frac{dC_t}{C_{t^-}} = \mu_Cdt+\sigma_C^\top dB_t + \sum_{j=1}^n(e^{-\zeta_C^{(j)}}-1)dN_t^{(j)},
\end{equation}$$ for constants $\mu_C\in\mathbb{R}$, $\sigma_C\in\mathbb{R}^m$, and $\zeta_C^{(j)}\in\mathbb{R}$. In equilibrium, agent $i$'s consumption process $C_i\in\mathcal{C}$ solves the stochastic differential equation $$\begin{multline}
\frac{dC_{it}}{C_{it^-}} = \mu_C^{(i)}(C_t,\Theta_t,X_t)dt+\sigma_C^{(i)}(C_t,\Theta_t,X_t)^\top dB_t + \sum_{j=1}^n(e^{-\zeta_C^{(i,j)}(C_{t^-},\Theta_{t^-},X_{t^-})}-1)dN_{t}^{(j)} \\
+ \tilde{\sigma}(X_t)dB_{it} + (e^{-\tilde{\zeta}(X_{t^-},\tilde{Z}_t)}-1)(dN_{it}-\eta(X_t)dt)
\label{eq:idioconsumpprocess_setting}
\end{multline}$$ with initial condition $C_{i0}>0$. The random variable $\tilde{Z}_t$ is drawn from time-invariant distribution $\tilde{\nu}$. Moreover, the functions $\mu_C^{(i)}$, $\sigma_C^{(i)}$, $\zeta_C^{(i,j)}$, $\tilde{\sigma}$, and $\tilde{\zeta}$, and the random variable $\tilde{Z}_t$ satisfy the necessary conditions for $C_i$ to be unique.*

One can think of aggregate consumption as an exogenous endowment or endogenous total output, and each individual's consumption as the equilibrium decision *after* receiving income and making optimal investment decisions. While it may not be obvious at this point, take note that cross-sectional risk $X$ will only affect the coefficients $\mu_{Ct}^{(i)}$, $\sigma_{Ct}^{(i)}$, and $\zeta_{Ct}^{(i,j)}$ when markets are incomplete. Cross-sectional risk is originating in the idiosyncratic risk coefficients $\tilde{\sigma}_t$, $\tilde{\zeta}_t$ and $\eta_t$, then potentially affecting the distribution of consumption growth when these risks cannot be insured away. Whether this is in fact the case is to be determined after agents' preferences and the securities market are specified.

Assumption 4 contains two helpful but nonessential simplifications. First, aggregate consumption growth is assumed to be independent and identically distributed, so that we can focus solely on cross-sectional risks. Second, exposure of individual agents to idiosyncratic risks is assumed to be ex ante identical: $\tilde{\sigma}_t$ and $\tilde{\zeta}_t$ are the same for all agents. The framework generalizes straightforwardly to both time-varying aggregate growth dynamics and heterogeneous exposures to idiosyncratic shocks without changing the core economics.

Having described the consumption process of each agent, we need also to define the preferences of each agent that, in equilibrium, yield this process. To make my main point about the pricing of idiosyncratic risks, it suffices to endow agents with identical isoelastic recursive preferences. This is the most practically relevant case; nevertheless, the core results generalize to a much broader class of heterogeneous recursive preferences.

**Assumption 5** (Preferences). *The felicity function $\bar{f}^{(i)}:\mathcal{C}\times\mathbb{R}\to\mathbb{R}$ of each agent $i\in\mathcal{I}$ takes the identical form $$\begin{equation}
\bar{f}(c,v) = \begin{cases}
\dfrac{\rho}{1-1/\psi}(1-\gamma)v\left(\left(\dfrac{c}{\left((1-\gamma\right)v)^{1/(1-\gamma)}}\right)^{1-1/\psi}-1\right) &\textrm{if}\quad \psi\neq1, \\
\rho(1-\gamma)v\left(\log{c}-\dfrac{\log{((1-\gamma)v)}}{1-\gamma}\right) &\textrm{if}\quad \psi=1.
\end{cases}
\label{eq:aggregator_special}
\end{equation}$$*

In ([\[eq:aggregator_special\]](#eq:aggregator_special)), we can interpret $\rho$ as the rate of time preference, $\psi$ as the elasticity of intertemporal substitution (EIS), and $\gamma$ as the coefficient of relative risk aversion. This specific form of felicity, derived by , corresponds to the continuous-time adaptation of the recursive preferences proposed by and . Under these preferences, there exists a unique process $V_i$, which we will call the *value function* process of agent $i$, such that $$\begin{equation}
V_{it} = \mathbb{E}_t\left[\int_t^\infty \bar{f}(C_{is},V_{is})ds\right].
\label{eq:valuefunc_setup}
\end{equation}$$ When $\gamma=1/\psi$, we get the special cases of time-additive power or log utility, $$\begin{equation}
\bar{f}(c,v) = u(c) - \rho v = \begin{cases}
\rho\log{c}-\rho v &\textrm{if}\quad \gamma=1, \\
\rho\dfrac{c^{1-\gamma}}{1-\gamma}-\rho v &\textrm{otherwise},
\end{cases}
\label{eq:aggregator_timeadd_special}
\end{equation}$$ which implies the usual explicit value function: $$V_{it} = \mathbb{E}_t\left[\int_t^\infty e^{-\rho(s-t)}u(C_{is})ds\right].$$ Henceforth, assume that $\gamma>1$ except in the case of time-additive log utility.

Finally, I make the following assumption about the set of securities in which agents trade.

**Assumption 6** (Securities). *There exists a riskfree asset, the *bond*, with instantaneous return $r_t$. There are also $m+n$ risky assets, the *stocks*, each of which is a claim to a stream of cash flows given by the stochastic process $D^{(k)}$, $k\in\{1,\dots,m+n\}$, called the *dividend process* for stock $k$. The dividend process $D^{(k)}$ satisfies the stochastic differential equation $$\begin{equation}
\frac{dD_t^{(k)}}{D_{t^-}^{(k)}}=\mu_D^{(k)}dt+\sigma_D^{(k)\top}dB_t + \sum_{j=1}^n(e^{-\zeta_{D}^{(k,j)}}-1)dN_{t}^{(j)}
\label{eq:ddividend_setup}
\end{equation}$$ with initial condition $D_{0}^{(k)}>0$. The constants $\mu_D^{(k)}$, $\sigma_D^{(k)}$, and $\zeta_{D}^{(k,j)}$ satisfy the necessary conditions for each $D^{(k)}$ to be unique. Moreover, all dividend processes are non-redundant (linearly independent). In equilibrium, agents' allocations to these assets are not constrained by any quantity restrictions. There are no arbitrage opportunities.*

One could easily generalize the coefficients $\mu_D^{(k)}$, $\sigma_D^{(k)}$, and $\zeta_{D}^{(k,j)}$ to be time-varying functions of $X$; it would have no bearing on the main results that follow.

Let $S_t^{(k)}$ represent the time-$t$ price of the $k$th stock. Denote the stock's return by $$dR_{St}^{(k)} = \frac{D_t^{(k)}}{S_t^{(k)}}dt + \frac{dS_t^{(k)}}{S_{t^-}^{(k)}},$$ the sum of its dividend yield and capital gains. The expected return is thus $r_{St}^{(k)} = \mathbb{E}_t[dR_{St}^{(k)}]/dt$. The expected excess return, or *risk premium*, is then $r_{St}^{(k)}-r_t$.

This is not necessarily a complete description of the securities market in the economy; rather, these are the assets we would like to price. The assumption of $m+n$ non-redundant stocks --- as opposed to, say, a single stock --- is made solely so that it is easy to compare this incomplete-market economy with a complete-market benchmark. This is because completing the market requires, at least, that all systematic consumption risks are spanned by the set of available stocks. We are interested in the effects of unspanned idiosyncratic risks. To emphasize that this assumption is not central, I will henceforth suppress the $k$ indexing and refer to an arbitrary risky security in this set as *the stock*. Let us now solve for the returns on the riskfree bond and the stock in this economic setting. To do this, we must first derive some intermediate results characterizing equilibria.

## Equilibrium conditions 

Equilibrium consumption plans and asset returns are jointly determined by two conditions. First, given the menu of available securities, the consumption processes $C_i$ are such that lifetime utility $V_{it}$ is indeed at a maximum. Second, prices of available securities do not admit arbitrage opportunities. This section establishes the consequences of these two conditions.

Because all processes are Markov, we can characterize the value function $V_{it}$ as some function $J(C_{it},X_t)$.[^14] From this characterization, we can define the *marginal felicity of consumption* $$f^{(i)}_{Ct}=f_C(C_{it},X_t)=\frac{\partial \bar{f}(C_{it},V_{it})}{\partial C_{it}}\bigg|_{V_{it}=J(C_{it},X_t)},$$ and, analogously, the *marginal felicity of value* $$f^{(i)}_{Vt}=f_V(C_{it},X_t)=\frac{\partial \bar{f}(C_{it},V_{it})}{\partial V_{it}}\bigg|_{V_{it}=J(C_{it},X_t)}.$$ These objects are critical to pricing assets because, as the following lemma shows, they determine the *state-price density* of each agent $i\in\mathcal{I}$. Letting $\pi_i=\{\pi_{it}:t\geq0\}$ denote these state-price density processes, standard asset pricing results imply the following.

**Lemma 1** (State-price densities). *In equilibrium, the state-price density of agent $i$ takes the form $$\begin{equation}
\pi_{it} = \exp{\left\{\int_0^tf_V(C_{is},X_s)ds\right\}}f_C(C_{it},X_t).
\label{eq:statepricedensity_theory}
\end{equation}$$ By the absence of arbitrage and portfolio constraints, the instantaneous riskfree rate $$\begin{equation}
r_t = -\mathbb{E}_t\left[\frac{d\pi_{it}}{\pi_{it^-}}\right]\frac{1}{dt}.
\label{eq:riskfreerate_general_theory}
\end{equation}$$ For any asset with dividend process $D$ and price process $S$ satisfying $$\begin{equation}
\frac{dS_t}{S_{t^-}} = \mu_{St}dt + \sigma_{St}^\top dB_t + \sum_{j=1}^n(e^{-\zeta_{St}^{(j)}}-1)dN_t^{(j)},
\label{eq:dstockprice_theory}
\end{equation}$$ the expected excess return $$\begin{equation}
r_{St}-r_t = -\mathbb{E}_t\left[\frac{d[\pi_i,R_S]_t}{\pi_{it^-}}\right]\frac{1}{dt} = -\mathbb{E}_t\left[\frac{d[\pi_i,S]_t}{\pi_{it^-}S_{t^-}}\right]\frac{1}{dt}. 
\label{eq:riskpremium_general_theory}
\end{equation}$$*

The state-price density expression ([\[eq:statepricedensity_theory\]](#eq:statepricedensity_theory)) evolves according to $$\frac{d\pi_{it}}{\pi_{it^-}} = f_{Vt}^{(i)}dt + \frac{df_{Ct}^{(i)}}{f_{Ct^-}^{(i)}},$$ meaning that unexpected shocks to the discount factor $\pi_i$ are, ultimately, unexpected changes in the agent's marginal felicity of consumption. Combining this intuition with the excess return relation ([\[eq:riskpremium_general_theory\]](#eq:riskpremium_general_theory)) implies that risks are priced if and only if those risks arrive in the form of correlated shocks to both marginal felicity $f_C$ and the stock return $R_S$. Our main question of interest boils down to exactly when this is and is not the case.

In principle, this characterization of agents' state-price densities is enough to study equilibrium return dynamics. Under our assumption of isoelastic preferences, though, we can say more about these state-price densities by solving explicitly for the value function.

**Lemma 2** (Consumption and value function). *Suppose the $n+m$ stocks defined in Assumption 6 satisfy equations of the form ([\[eq:dstockprice_theory\]](#eq:dstockprice_theory)). Then all agents have identical exposure to aggregate consumption shocks: for all $i\in\mathcal{I}$, ([\[eq:idioconsumpprocess_setting\]](#eq:idioconsumpprocess_setting)) holds with $$\mu_{Ct}^{(i)} = \mu_C, \quad \sigma_{Ct}^{(i)} = \sigma_C, \quad\textrm{and}\quad \zeta_{Ct}^{(i,j)} = \zeta_C^{(j)}.$$ Additionally, the value function of each agent $i\in\mathcal{I}$ takes the form $$\begin{equation}
V_{it}=J(C_{it},X_t) = \frac{C_{it}^{1-\gamma}I(X_t)^{1-\gamma}}{1-\gamma},
\label{eq:valuefuncconject_theory}
\end{equation}$$ where the function $I(x)$ solves the ordinary differential equation ([\[eq:hjbconject_theory\]](#eq:hjbconject_theory)).*

Given this result, we have that the marginal felicity of consumption is $$f_C(c,x) =  \rho I(x)^{1/\psi-\gamma}c^{-\gamma},$$ and the marginal felicity of value is $$f_V(c,x) = f_V(x) = \begin{cases}
-\rho\left(1+\left(\dfrac{\gamma-1/\psi}{1-1/\psi}\right)(I(x)^{1/\psi-1}-1)\right) & \textrm{if}\quad \psi\neq1, \\
-\rho\left(1+(1-\gamma)\log{I(x)}\right) & \textrm{if}\quad \psi=1.
\end{cases}$$ Both of these expressions are functions of $X$ if and only if $\gamma\neq1/\psi$ --- that is, if and only if agents do not have time-additive power or log utility.

Both of the lemmas above require that the risky assets we are trying to price --- namely, the stocks defined in Assumption 6 --- satisfy stochastic differential equations of the form ([\[eq:dstockprice_theory\]](#eq:dstockprice_theory)). The following lemma confirms this and characterizes these prices.

**Lemma 3** (Stock price). *The price of the stock is given by $$S_t = D_tF(X_t)$$ and solves the stochastic differential equation ([\[eq:dstockprice_theory\]](#eq:dstockprice_theory)) with $\mu_{St}$ given by ([\[eq:equitydrift_theory\]](#eq:equitydrift_theory)), $$\begin{equation}
\sigma_{St} = \sigma_{D} + \frac{F_{Xt}}{F_t}\sigma_{Xt},
\label{eq:equitydiffusion_theory}
\end{equation}$$ and $$\begin{equation}
e^{-\zeta_{St}^{(j)}} = e^{-\zeta_{D}^{(j)}}\left(\frac{F(X_{t^-}+\zeta_{Xt}^{(j)})}{F(X_{t^-})}\right).
\label{eq:equityjump_theory}
\end{equation}$$ The price-dividend ratio $F(x)$ is the solution to the ordinary differential equation ([\[eq:equitypde_theory\]](#eq:equitypde_theory)).*

This fact verifies that we can fully apply Lemmas 1 and 2 in our setting. The expressions ([\[eq:equitydiffusion_theory\]](#eq:equitydiffusion_theory)) and ([\[eq:equityjump_theory\]](#eq:equityjump_theory)) also show us how cross-sectional risk may directly affect equity risks. When the price-dividend ratio $F$ is a function of $X$, the stock's volatility is affected by both Brownian and Poisson shocks to cross-sectional risk.

## Asset pricing solutions 

### The complete-market economy 

To make a statement about the consequences of market incompleteness, it is necessary to define an economy in which markets are complete and agents do not face idiosyncratic risks.

**Definition 1**. *We say that an economy is *essentially complete* if $$\pi_{it} = \pi_{i't}$$ almost surely, for all agents $(i,i')\in\mathcal{I}\times\mathcal{I}$ and all $t\geq0$. Let $\pi^{\rm CM}$ denote the common state-price density process in such an economy. The *complete-market economy* is the set of essentially complete economic settings satisfying the assumptions in Section 2.1.*

This definition takes advantage of the well-known asset pricing result that state-price densities of unconstrained investors are equated in a complete-market equilibrium (Duffie 2010). Essential completeness means that consumption allocations are Pareto optimal, so that adding new securities to the economy is never welfare-improving. Note that essential completeness is a weaker definition than completeness, which requires that any consumption plan can be financed by an admissible trading strategy. Completeness implies essential completeness, but not vice versa.[^15] One can show that, in our isoelastic setting, essential completeness is equivalent to the absence of idiosyncratic risks ($\tilde{\sigma}_t=\tilde{\zeta}_t\eta_t=0$) for all agents. This, in turn, implies that $X$ is no longer a state variable.

Using the equilibrium conditions derived in the previous section, we can immediately solve for asset prices in this economy.

**Proposition 1**. *In the complete-market economy, the equilibrium riskfree rate equals $$\begin{multline}
r^{\rm CM} = \rho + \frac{1}{\psi}\mu_C - \frac{1}{2}\gamma\left(\frac{1}{\psi}+1\right)|\sigma_C|^2 \\
-\sum_{j=1}^n\lambda^{(j)}\left[e^{\gamma \zeta_C^{(j)}}\left(1-\frac{1/\psi-\gamma}{1-\gamma}e^{-\zeta_C^{(j)}}\right) - \frac{1-1/\psi}{1-\gamma}\right].
\label{eq:riskfreerate_cm_theory}
\end{multline}$$*

This interest rate is the same as that which arises from a representative agent endowed with aggregate consumption (Tsai and Wachter 2018). The expression captures the standard consumption-based asset pricing intuition: the riskfree rate is increasing in impatience $\rho$ and expected growth $\mu_C$, due to the intertemporal tradeoff; and decreasing in systematic risks $\sigma_C$ and $\zeta_C^{(j)}$, due to precautionary savings. These effects are mediated by both risk aversion $\gamma$ and the EIS $\psi$. The interaction of these motives can be complicated, especially in the jump terms where growth effects and precautionary savings demand enter non-linearly; nevertheless, we can reduce intuition to two important cases. The first is whether agents have a preference for early ($\gamma>1/\psi$) or late ($\gamma<1/\psi$) resolution of uncertainty: this governs agents' attitudes toward future consumption risks. The second is whether the elasticity of substitution is above, below, or equal to one: this determines the sensitivity of the interest rate to growth expectations due to competing wealth and substitution effects.

Similarly, we can solve for the price of the stock and its expected excess return.

**Proposition 2**. *In the complete-market economy, the risk premium on the stock equals $$\begin{equation}
r_S^{\rm CM}-r^{\rm CM} =  \gamma\sigma_C^\top\sigma_S^{\rm CM} + \sum_{j=1}^n\lambda^{(j)}\left[\left(e^{\gamma\zeta_C^{(j)}}-1\right)\left(1-e^{-\zeta_S^{({\rm CM},j)}}\right)\right],
\label{eq:riskpremium_cm_theory}
\end{equation}$$ where the equity-risk coefficients $$\begin{equation*}
\sigma_S^{\rm CM} = \sigma_{D} \quad\textrm{and}\quad e^{-\zeta_S^{({\rm CM},j)}} = e^{-\zeta_{D}^{(j)}}.
\end{equation*}$$*

Like the interest rate, the equilibrium excess return is a standard result for complete-market economies with jumps. The first term on the right-hand side is the classic consumption-CAPM: agents demand compensation for systematic Brownian consumption risks that covary positively with the stock return. In a complete market, the volatility of the stock return is just the volatility of the underlying cash flows. The exact same reasoning applies to the jump terms: agents demand a risk premium if aggregate consumption and the stock price (and dividends) jump downward at the same time.

With these results in hand, we can now make claims about the interesting case in which idiosyncratic risks cannot be insured.

### The incomplete-market economy 

We will define the *incomplete-market economy* as the set of equilibria satisfying the assumptions in Section 2.1 that are not encompassed by the complete-market economy.[^16] Using the equilibrium state-price densities and return relations derived in Section 2.2, we can solve for the riskfree rate in this economy, and see how it is affected by cross-sectional risk and recursive preferences.

**Proposition 3**. *In the incomplete-market economy, the equilibrium riskfree rate equals $$\begin{multline}
r_t = \rho + \frac{1}{\psi}\mu_C - \frac{1}{2}\gamma\left(\frac{1}{\psi}+1\right)(|\sigma_C|^2+\tilde{\sigma}(X_t)^2) \\
+ \frac{1}{2}\left(\gamma-\frac{1}{\psi}\right)\left(\frac{1}{\psi}-1\right)\left(\frac{I_{X}(X_t)}{I(X_t)}\right)^2|\sigma_X(X_t)|^2 \\
-\sum_{j=1}^n\lambda^{(j)}\left[e^{\gamma \zeta_C^{(j)}}\left(\frac{I(X_t+\zeta_{Xt}^{(j)})}{I(X_t)}\right)^{1-\gamma} \left(1-\frac{1/\psi-\gamma}{1-\gamma}e^{-\zeta_C^{(j)}}\right) - \frac{1-1/\psi}{1-\gamma}\right] \\
- \eta(X_t)\mathbb{E}_{\tilde{\nu}}\left[\left(e^{\gamma\tilde{\zeta}_t}-\frac{1}{\psi}\right)\left(1-\frac{1/\psi-\gamma}{1-\gamma}e^{-\tilde{\zeta}_t}\right) - \frac{1-1/\psi}{1-\gamma}\right].
\label{eq:riskfreeratethm1_1_theory}
\end{multline}$$*

Two main insights emerge from ([\[eq:riskfreeratethm1_1_theory\]](#eq:riskfreeratethm1_1_theory)). First, agents' precautionary savings motives from idiosyncratic risks ($\tilde{\sigma}$, $\tilde{Z}$, and $\eta$) aggregate to have a direct effect on interest rates, even if these risks are static. This is perhaps most apparent in the case of time-additive power utility ($\gamma=1/\psi$), for which the interest rate becomes $$r_t = r^{\rm CM} - \frac{1}{2}\gamma(\gamma+1)\tilde{\sigma}_t^2 - \eta_t\mathbb{E}_{\tilde{\nu}}\left[e^{\gamma\tilde{\zeta}_t}-\gamma-1\right].$$ The latter two terms, which do not appear in the complete-market riskfree rate, are non-zero, even if $X$ is a constant. Thus, market incompleteness can drive down interest rates. Second, when cross-sectional risk $X$ is time-varying, the riskfree rate may also respond to movements in $X$. Whether and in which direction this is the case depends, again, on two key attributes: the preference over timing of resolution of uncertainty ($\gamma$ relative to $1/\psi$) and the relative strengths of the wealth and substitution effects ($\psi$ relative to unity). The second line in equation ([\[eq:riskfreeratethm1_1_theory\]](#eq:riskfreeratethm1_1_theory)) shows us that, if felicity is non-time-additive and the EIS is not equal to one, then time-variation in cross-sectional risk through a non-zero $\sigma_X$ will necessarily have an effect on the interest rate. A similar term for $\zeta_X^{(j)}$ shows up non-linearly in the jump term.

Now consider risk premia in this economic setting.

**Proposition 4**. *In the incomplete-market economy, the risk premium on the stock equals $$\begin{multline}
r_{St}-r_t =  \gamma\sigma_C^\top\sigma_{St} + \left(\gamma-\frac{1}{\psi}\right)\frac{I_X(X_t)}{I(X_t)}\sigma_{Xt}^\top\sigma_{St}\\
+ \sum_{j=1}^n\lambda^{(j)}\left[\left(e^{\gamma\zeta_C^{(j)}}\left(\frac{I(X_{t^-}+\zeta_{Xt}^{(j)})}{I(X_{t^-})}\right)^{1/\psi-\gamma}-1\right)\left(1-e^{-\zeta_{St}^{(j)}}\right)\right],
\label{eq:riskpremiumthm1_theory}
\end{multline}$$ where the equity-risk coefficients $\sigma_{St}$ and $\zeta_{St}^{(j)}$ are given by ([\[eq:equitydiffusion_theory\]](#eq:equitydiffusion_theory)) and ([\[eq:equityjump_theory\]](#eq:equityjump_theory)), respectively.*

As with the riskfree rate, we see new terms relating to time-varying cross-sectional risk. Consider the second term on the right-hand side of ([\[eq:riskpremiumthm1_theory\]](#eq:riskpremiumthm1_theory)): aversion to cross-sectional risk times the covariance of Brownian shocks to $X$ and the stock return. Suppose, as we will in the human-capital model in Section 3, that agents have non-time-additive utility with a preference for early resolution of uncertainty ($\gamma>1/\psi$). Suppose also that cross-sectional risk is "bad,\" in that it decreases the continuation value ($I_X/I<0$); and that it increases in "bad times,\" in that it is negatively correlated with the stock ($\sigma_X^\top\sigma_S<0$). Then this term contributes positively to the equity risk premium, as agents demand compensation for the effect of time-varying uninsurable risks on future idiosyncratic consumption growth. Despite an i.i.d. aggregate endowment, idiosyncratic risks are priced.

That this second term appears is consistent with previous claims that non-time-additive preferences can restore the relevance of market incompleteness in continuous time. What might be surprising about this result, though, is that the intuition remains identical even in the presence of correlated *jumps* to $X$, $C$, and $S$. That is, the jump terms depend in exactly the same way on preferences ($\gamma,1/\psi,I$) and the correlation of risks ($\zeta_X^{(j)}\zeta_S^{(j)}$). There is no interaction term between jumps and Brownian risks, even though the volatilities $\sigma_X$ and $\tilde{\sigma}$ may be subject to an arbitrary number of jumps over any small time interval. This intuition will be formalized below.

We also see a second possible channel for relevance of cross-sectional risk: equity risk coefficients $\sigma_S$ and $\zeta_S^{(j)}$ need not equal $\sigma_S^{\rm CM}$ and $\zeta_S^{({\rm CM},j)}$ if cross-sectional risk is stochastic ($\sigma_X$ or $\zeta_X^{(j)}$ are non-zero) and the price-dividend ratio $F$ is a function of $X$. In this case, cross-sectional risk could become a source of excess volatility above that which is generated by risky cash flows. Jumps, again, introduce no new economic channels that are not analogous to those arising from Gaussian risks.

## When does idiosyncratic risk matter? 

The effect of market incompleteness on returns will depend critically on whether cross-sectional risk is stochastic and on the assumed form of agents' felicity functions. We begin with a definition regarding our key state variable.

**Definition 2**. *We say that cross-sectional risk $X$ is *stochastic* if it is not the case that, almost surely, $\sigma_X(X_t)=\zeta_X^{(j)}(X_{t^-})=0$ for all $j\in\{1,\dots,n\}$. We say that $X$ is *time-varying* if it is stochastic or $\mu_X(X_t)\neq0$.*

Recall that, even if cross-sectional risk is non-time-varying, it may still be relevant for asset prices, as agents demand precautionary savings to buffer against static idiosyncratic risks. Moreover, recall from the expected return expressions that non-time-additive utility ($\gamma\neq1/\psi$) renders cross-sectional risk a priced factor. This is not just about preference for early or late resolution of uncertainty; it is a consequence of the more general property that marginal felicity of today's consumption is dependent on the continuation value $V$.[^17] In the present case of isoelastic preferences, marginal felicity depends on $X$ if and only if $\gamma\neq1/\psi$ and $X$ is time-varying (in which case $I(X_t)$ does not reduce to a constant).

Now let us address the central question: when do incomplete markets matter for risk premia? I consider two notions of relevance, differentiated by their assumptions about equity-return risks. The first is the notion: imposing that equity risks are identical in the complete- and incomplete-market economies (fixing $\{\sigma_S,\{\zeta_S^{(j)}\}_{j=1}^n\}=\{\sigma_S^{\rm CM},\{\zeta_S^{({\rm CM},j)}\}_{j=1}^n\}$), when does incompleteness matter? This question amounts to whether and when cross-sectional risks affect risk premia through the state-price densities, or *price of risk*, of investors. This first notion is formally defined as follows.

**Definition 3**. *We say that *market incompleteness is relevant for risk premia through the price of risk* if equity risk premia in the incomplete- and complete-market economies are not identical, given that the stock-return coefficients $\sigma_S=\sigma_S^{\rm CM}$ and $\zeta_S^{(j)}=\zeta_S^{({\rm CM},j)}$ almost surely.*

The second notion, which is more complete and therefore arguably more informative, is the case in which we allow equity risks to differ between the two types of economies, as they should in general equilibrium. In this case, both prices of risks and endogenous equity risks (return volatility) can be affected by market incompleteness.

**Definition 4**. *We say that *market incompleteness is irrelevant for risk premia* if equity risk premia in the incomplete- and complete-market economies are not identical, given the stock return processes $\{\sigma_S,\{\zeta_S^{(j)}\}_{j=1}^n\}$ and $\{\sigma_S^{\rm CM},\{\zeta_S^{({\rm CM},j)}\}_{j=1}^n\}$ determined in their respective equilibria (i.e., as stated in Propositions 2 and 4).*

The reason for these separate concepts is subtle but important in light of the literature on heterogeneous-agent asset pricing. The well-known arguments of and assume the former: they characterize risk premia, taking the return processes on the risky assets as some exogenously given process.[^18] This partial-equilibrium perspective informs us about how agents demand compensation for the risks they face. Taking the stock's volatility and jump magnitudes as given may also be a reasonable starting point for empirical tests of state-price densities. However, in reality, the return process is an endogenous object, and so, even if this statement holds, these types of results give us no guarantee that covariances of state-price densities with price changes will be the same in an incomplete market. Indeed, considering the endogenous effect of market incompleteness on equity risk is essential to explaining why stock returns are so volatile in the first place (Shiller 1981). This is why the second notion of relevance is more informative.

In light of these views, I now lay out two analogous theorems, which elucidate exactly when market incompleteness matters.

**Theorem 1**. *Market incompleteness is relevant for risk premia through the price of risk if and only if both of the following conditions hold:*

1.  *Cross-sectional risk is stochastic and correlated with the stock.*

2.  *Felicity is non-time-additive (i.e., $\gamma\neq1/\psi$).*

Countercyclical cross-sectional risk, the first of these two conditions, is the core assumption of virtually all incomplete-markets-based asset pricing models. It has been validated by both income and consumption data. The theorem tells us that, given such risks and holding fixed the distribution of equity-price shocks, the *only* way in which market incompleteness can explain the equity premium is if agents have non-additive preferences. Even with an arbitrary number of Poisson jumps, the question of whether agents demand risk compensation reduces to a question of their intertemporal preferences.

It is in this sense that the model of ceases to operate in continuous time. Because agents have time-additive power utility, Theorem 1 implies that even stochastic cross-sectional risk that is correlated with the stock return cannot increase the equity risk premium. Jumps make no difference, as the next subsection discusses in more detail. In contrast, Theorem 1 suggests that one part of the argument of continues to hold in continuous time, because they assume both countercyclical cross-sectional risk and non-separable preferences.

Now, consider the endogenous-return extension of this theorem.

**Theorem 2**. *Market incompleteness is relevant for risk premia if and only if both of the following conditions hold:*

1.  *Cross-sectional risk is stochastic.*

2.  *At least one of the following is true:*

    - *Felicity is non-time-additive (i.e., $\gamma\neq1/\psi$).*

    - *Aggregate consumption shocks are correlated with shocks to cross-sectional risk (i.e., it is not the case that $\sigma_C^\top\sigma_{Xt}=\zeta_C^{(j)}\zeta_{Xt}^{(j)}=0$ almost surely).*

As before, cross-sectional risk must be stochastic. Under this more general notion, though, two distinctions arise from the equity-risk channel. First, cross-sectional risk can affect risk premia simply by being correlated with aggregate consumption risk; non-time-additive preferences are sufficient, but no longer necessary. The reason is that stochastic cross-sectional risks (the coefficients $\sigma_X$ and $\zeta_X^{(j)}$) always affect equity risks (the coefficients $\sigma_S$ and $\zeta_S^{(j)}$) --- recall ([\[eq:equitydiffusion_theory\]](#eq:equitydiffusion_theory)) and ([\[eq:equityjump_theory\]](#eq:equityjump_theory)). In other words, stock prices endogenously inherit shocks to cross-sectional risk, so these processes become naturally correlated. Consider, for illustration, the risk premium ([\[eq:riskpremiumthm1_theory\]](#eq:riskpremiumthm1_theory)) in the special case of time-additive utility and no jumps: $$r_{St}-r_t = \gamma\sigma_C^\top\sigma_{St} = \underbrace{\gamma\sigma_C^\top\sigma_S^{\rm CM}}_{r_S^{\rm CM}-r^{\rm CM}} + \gamma\frac{F_{Xt}}{F_t}\sigma_C^\top\sigma_{Xt}.$$ Even under power utility, the risk premium differs in an incomplete market if $\sigma_C^\top\sigma_{Xt}\neq0$.[^19] The second, related distinction between the theorems is that Theorem 2 omits from its first condition the statement that stochastic cross-sectional risks must be correlated with stock returns. The reasoning is the same as above: equity returns are endogenously correlated with stochastic cross-sectional risks. If condition 2(b) does not hold, the question again becomes whether agents demand compensation for these correlated risks through non-separable preferences, as in Theorem 1.

With this new theoretical result, we can restate and better understand well-known irrelevance results within this more general framework. Let us first consider the classic result of .

**Corollary 1** (Generalized Grossman & Shiller). *If all agents $i\in\mathcal{I}$ have time-additive power utility, then market incompleteness is irrelevant for risk premia, holding equity risks fixed.*

This is effectively the same statement made in their paper, with an additional layer of generality: their argument continues to hold even when we add an arbitrary number of jumps in both the state variable and consumption.

Additionally, the theorems bear out implications for the discrete-time irrelevance result of . These authors show that, assuming power utility and i.i.d. aggregate consumption growth that is uncorrelated with cross-sectional risk, market incompleteness is irrelevant for risk premia. A generalized continuous-time form of their conclusion is implied by the theorems in this paper.

**Corollary 2** (Continuous-time Krueger & Lustig). *Suppose all agents have identical power or log utility and aggregate consumption growth is i.i.d. Then market incompleteness is irrelevant for risk premia if and only if aggregate consumption shocks are uncorrelated with cross-sectional risk shocks.*

Zero correlation between the aggregate endowment and cross-sectional risk is not only sufficient, but also necessary for general-equilibrium irrelevance. Moreover, both irrelevance theorems emphasize that this is specific to additive utility. Even with completely uncorrelated aggregate risks, non-time-additive preferences necessarily alter the risk premium.

## Discussion: The irrelevance of jumps

Both of these theorems yield a novel insight about Poisson jumps: they have no bearing on the relevance of market incompleteness. This is striking, considering that previous studies have claimed the opposite. I show how these views can be reconciled.

The hypothesis that jumps can recover the mechanism as time becomes continuous is predicated on the following intuition. In , changes in cross-sectional risk $X$ over a time interval of measure $\Delta$ are normally distributed. Idiosyncratic consumption shocks arrive as $\tilde{\sigma}(X_{t+\Delta})$ times an i.i.d. $N(0,\Delta)$ random variable. Investors demand compensation if shocks to $X_{t+\Delta}-X_t$ co-occur with stock returns. As $\Delta$ declines to zero, though, Gaussian shocks become Brownian motions and $\tilde{\sigma}(X_{t+\Delta})$ becomes locally deterministic, so this co-occurrence disappears. The claim, then, is that one can overcome this limiting deterministic behavior by allowing for *jumps* in $X$ (and therefore jumps in $\tilde{\sigma}$) that occur simultaneously with jumps in the stock price. In the terminology of the present framework, one expects to see a covariance term relating $\tilde{\sigma}(X_{t^-}+\zeta_{Xt})$ to the simultaneous stock-price jump $\zeta_{St}$.

But the results above imply that agents do not demand compensation for such jumps. Why is this so? The reason, in short, is that this is a measure-zero event. The above intuition requires an ordered sequence of jumps: first there is a jump in $X$, which then yields a jump in $\tilde{\sigma}$, which then scales agents' idiosyncratic Brownian shocks $dB_i$. Such a sequence is impossible, as each Poisson process is of finite variation and can therefore only jump once over an infinitesimal time interval. It is not enough to have discontinuous sample paths in $X$; it is not even enough to have an arbitrary number $n$ of jumps.

Fortunately, this finding can be reconciled with previous studies that have posited the jump intuition (Martin 2013; Panageas 2020). This kind of multi-jump event is possible under a less conventional class of stochastic processes with uncountably many jumps. Including such jump processes broadens the notion of uncertainty to the full set of so-called Lévy processes (Protter 1992; Cont and Tankov 2004). In a recent survey article, does exactly this: assuming that cross-sectional risk depends on a variance gamma process (an infinite-activity Lévy process) he shows that the mechanism used by can be recovered in the continuous-time limit. In fact, the variance gamma example of falls under a subset of infinite-jump processes, called *subordinated Brownian motions*, which have been studied at length in the mathematical finance literature.[^20] Subordinated Brownian motions are Brownian motions on a transformed time scale, such that, over the true time scale, they become an infinite-variation series of jumps. As show, two especially tractable special cases of this are Brownian motions subordinated to variance gamma and inverse Gaussian processes.

## Discussion: Additional insights 

Beyond irrelevance results, the framework above yields three insights that are worth briefly discussing, for the sake of completeness.

In addition to risk premia, I characterize the effect of market incompleteness on two central asset pricing moments: equity volatility and the riskfree interest rate. Unlike risk premia, these variables are always affected by countercyclical cross-sectional risk. This conclusion brings to light an interesting relationship between portfolio choice and asset prices. A large literature depends on the fact that idiosyncratic background risks, often coming from uninsurable labor-income shocks, explain low portfolio allocations to risky assets (Viceira 2001; Catherine 2020). In light of these irrelevance results, though, one might ask: how can idiosyncratic risk simultaneously decrease risky asset allocations and have no effect on risk premia? The answer is that, in general equilibrium, agents' aversion to uninsurable risks can show up entirely in equity volatility and the riskfree rate. The level of expected stock returns declines with the riskfree rate, volatility increases, but the premium is unchanged.

Second, this framework has cross-sectional asset pricing implications. Most conventional asset pricing models assume only Brownian risks and thus admit a linear factor structure. This fact is frequently exploited to justify reduced-form affine models and empirical analyses of stock returns in both the cross-section and time series. It follows from Proposition 4 that this is indeed the case when we assume that there are no jumps.

**Corollary 3** (CAPMs). *Suppose there are no jumps: $\zeta_C^{(j)}=\zeta_{Xt}^{(j)}=\zeta_{D}^{(j)}=0$ almost surely. The isoelastic economy admits a linear factor structure for the expected return on risky assets. Specifically, the expected excess return on the $k$th stock is given by a ICAPM: $$\begin{equation*}
r_{St}^{(k)}-r_t = \lambda_C\mathrm{Cov}_t\left(\frac{dC_t}{C_{t^-}},dR_{St}^{(k)}\right) + \lambda_{Xt}\mathrm{Cov}_t\left(dX_t,dR_{St}^{(k)}\right),
\end{equation*}$$ where the factor loadings $\lambda_C=\gamma$ and $\lambda_{Xt}=(\gamma-1/\psi)I_X(X_t)/I(X_t)$. If preferences are time-additive or $X$ is non-stochastic, then this economy admits the C-CAPM: $$\begin{equation*}
r_{St}^{(k)}-r_t = \gamma\mathrm{Cov}_t\left(\frac{dC_t}{C_{t^-}},dR_{St}^{(k)}\right).
\end{equation*}$$*

Provided that the price of cross-sectional risk $\lambda_{Xt}$ is non-zero, two stocks with the same exposure to aggregate consumption risk but different exposures to cross-sectional risk will earn different risk premia. This prediction of the model is in principle easily tested given cross-sectional return and consumption data.[^21] Indeed, find that a "common idiosyncratic volatility\" (CIV) factor --- the firm equivalent of cross-sectional risk in this framework --- is priced, so that stocks whose returns covary more negatively with CIV earn a higher risk premium. The CIV factor, they find, is highly correlated with labor-income risk, and therefore presumably also with the state variable $X$ in our model. Consequently, their empirical finding is consistent with this ICAPM factor model where $\gamma>1/\psi$ (preference for early resolution of uncertainty) and $I_X/I<0$ (cross-sectional risk is "bad\"). Indeed, this is exactly how the authors rationalize their findings: they propose a discrete-time model in which agents have isoelastic preferences and CIV jointly drives cross-sectional consumption and dividend risk.

Lastly, this general framework contains the particularly important special case of affine economies. For tractability, most asset pricing models assume that stochastic processes are affine in the given state variables. It is therefore worthwhile to extend the isoelastic economy to the special case in which coefficients that depend on $X$ are affine in $X$. This special case admits closed-form solutions where the more general economy leaves us with unsolved differential equations for $I(X)$ and $F(X)$. These solutions are also valuable because they can be used as a reference point for numerical solutions to non-affine economies.[^22] Appendix 8 contains a full derivation and discussion of asset pricing results in this affine economy. I move these informative results to an appendix because the human-capital model in the next section is an example of an affine economy, and so provides most insights.

## A more general theory 

The above framework is general, but does make the simplifying assumption that all agents have identical isoelastic preferences. One might wonder whether these irrelevance results are particular to this special case. In Section 10 of the Online Appendix, I generalize this theory to include a much broader class of recursive preferences and an arbitrary degree of cross-agent preference heterogeneity. Ultimately, none of the core findings above change. The conditions for irrelevance still depend on non-separable preferences and the correlation of shocks to aggregate consumption and cross-sectional risk. Jumps still have no consequence.

At least one interesting result does emerge from this generalized framework: identical power or log utility turns out to be one of the necessary and sufficient conditions for irrelevance of incomplete markets. This is due to three critical properties. First, as explained above, the time-additivity of these preferences means cross-sectional risks are not priced. Second, these preferences are isoelastic and homothetic, so that the level of individuals' consumption does not affect how they price risk and the bond. Third, when all agents have the same isoelastic preference parameters, consumption shares of individual agents are no longer a state variable. Together, these properties constitute a special case in which idiosyncratic risk can never affect risk premia.

# A model with inalienable human capital 

Theorem 2 shows us that stochastic cross-sectional risk can only affect risk premia through non-additive preferences or correlated risks to idiosyncratic and systematic consumption. The latter condition amounts to an increase in equity risk. Thus, this equity-risk channel can only explain asset pricing moments insofar as a consumption-CAPM with higher equity risk can explain them. Alternatively, preference non-additivity has the potential to fully explain both higher equity risk and higher effective risk aversion. To evaluate whether this is the case under realistic quantities, we need a quantitative model.

In this section, I solve and calibrate a heterogeneous-agent model in which agents have non-tradeable, hence uninsurable, human capital. The calibrated model quantitatively explains both asset prices and cross-sectional income skewness over time. This section has two purposes. First, it illustrates how the generalized framework above can be applied to a full general-equilibrium economy with production. In the previous sections, we took the equilibrium consumption processes as given; in this section, we will see how such a process can arise from the optimal consumption-portfolio choices of agents. Second, using data from the cross-section, I show how this tractable, parsimonious model can generate quantitatively realistic return dynamics that would be fully missed under a complete-market, representative-agent assumption. The price-of-risk channel is quantitatively important.

## Model setup 

Agents have identical recursive preferences with elasticity of intertemporal substitution (EIS) equal to one. In other terms, $$\begin{equation*}
\bar{f}(c,v) = \rho(1-\gamma)v\left(\log{c}-\frac{\log{((1-\gamma)v)}}{1-\gamma}\right),
\end{equation*}$$ for all agents $i\in\mathcal{I}$.

Agents have access to three investment opportunities: inalienable human capital, a riskfree bond, and a stock. Each agent is endowed with an initial quantity of human capital $H_{i0}$. This quantity may represent capitalized labor income, private business wealth of entrepreneurs, and other assets with concentrated or non-traded ownership. Human capital depreciates at a rate $\delta$ and produces the consumption good at a rate $a$. Let us denote the output (income) from agent $i$'s human capital by $Y_{it}=aH_{it}$. Agents can choose to invest in their own --- and only their own --- human capital at a rate $x_{it}$, yielding a percent increase in the capital stock of $\Phi(x_{it})=\frac{1}{\varphi}\log{(\varphi x_{it} + 1)}$.[^23] Investment is purchased in a capital investment market in exchange for output $Y_{it}$; in equilibrium, this market assigns an implicit price $q_{it}$ to the capital stock, meaning $q_{it}H_{it}$ represents the private market value of the asset. Finally, each agent's human capital is subject to stochastic quality shocks, some systematic and others idiosyncratic.[^24] Specifically, the "ex-dividend\" quantity of human capital solves the stochastic differential equation $$\begin{equation}
\frac{dH_{it}}{H_{it^-}} = (\Phi(x_{it})-\delta)dt +\underbrace{\sigma dB_{Ht} + (e^{-Z_t}-1)dN_{Ht}}_{\textrm{systematic capital shocks}} + \underbrace{\tilde{\sigma} dB_{it} + (e^{-\tilde{Z}_{it}}-1)(dN_{it} - \eta_{t}dt)}_{\textrm{idiosyncratic capital shocks}}.
\label{eq:idiocapitalprocess_model}
\end{equation}$$ The Brownian and Poisson shocks are defined exactly as in the preceding sections.[^25] Instead of having multiple aggregate jumps with deterministic magnitudes, I simplify notation by letting the jump intensity be determined by the random variable $Z_t$, which is drawn from time-invariant distribution $\nu$. The distribution of idiosyncratic disaster sizes $\tilde{\nu}$ is such that $\tilde{Z}_i$ tends to be positive. Consequently, realizations of the idiosyncratic jumps $dN_{it}$ tend to be adverse events --- "idiosyncratic disasters\" like persistent unemployment.

Agents face time-varying cross-sectional risk via stochasticity of the idiosyncratic jump probability $\eta_t$. In particular, this probability follows the square-root process (Cox et al. 1985)[^26] $$\begin{equation}
d\eta_t = \kappa_\eta(\bar{\eta}-\eta_t)dt+\sigma_\eta\sqrt{\eta_t}dB_{\eta t},
\label{eq:etaprocess_model}
\end{equation}$$ where constants are strictly positive and the Brownian motion $B_\eta$ is independent of all other shocks. Figure 1 shows the stationary distribution of $\eta$ over time, according to the model calibration below. This distribution is gamma with shape $2\kappa_\eta\bar{\eta}/\sigma_\eta^2$ and scale $\sigma_\eta^2/(2\kappa_\eta)$.

<figure id="fig:etadistribution" data-latex-placement="t">
<div class="center">
<img src="Calibration/Files/figures/lambdapdf" />
</div>
<figcaption>The figure shows the stationary distribution of the idiosyncratic disaster probability <span class="math inline"><em>η</em></span>, which solves <span class="math display">$$d\eta_t = \kappa_\eta(\bar{\eta}-\eta_t)dt+\sigma_\eta\sqrt{\eta_t}dB_{\eta t},$$</span> according to the calibration in Table <a href="#tab:calibtable" data-reference-type="ref" data-reference="tab:calibtable">[tab:calibtable]</a>. The solid line is the probability density function and the dashed vertical line is the unconditional mean <span class="math inline"><em>η̄</em> = 0.04</span>. The value of <span class="math inline"><em>η</em></span> is annual.</figcaption>
</figure>

Due to our assumption that there is a continuum of agents, the intensity $\eta$ has two interpretations. From the perspective of individual agents, it is, roughly speaking, the probability that human capital will experience a disaster shock. From the perspective of the macroeconomy, it determines the proportion of agents that will necessarily experience such a shock. In both views, we can interpret a higher $\eta_t$ as a higher degree of cross-sectional risk.

Agents cannot trade claims to each other's human capital and therefore are unable to insure against idiosyncratic risks. This is the main sense in which human capital is "inalienable\" and the market is incomplete in this model. I do assume, however, that agents can indirectly trade against their human capital by borrowing and lending in a zero-net-supply riskfree bond with instantaneous return $r_t$. We could interpret this as workers and entrepreneurs who borrow from retirees and rentiers at some market interest rate $r_t$ to finance their human capital or lever a position in the stock.[^27] Note that, because financial assets are in zero net supply, the aggregate quantity of capital in the economy will always equal $H_t=\int_\mathcal{I}H_{it}di$, which may vary over time with individual investment decisions $x_{it}$ but will be unaffected by either idiosyncratic quality shocks or leverage from trading the bond.

Finally, agents can trade with each other in an aggregate equity claim. Let us consider a claim to the dividend $D_t=Y_t^\phi$, where $Y_t= aH_t$ is aggregate output and $\phi\geq1$ represents leverage.[^28] Itô's lemma then implies that $$\begin{equation}
\frac{dD_{t}}{D_{t^-}} = \left(\phi(\Phi(x)-\delta)+\frac{1}{2}\phi(\phi-1)\sigma^2\right) dt + \phi\sigma dB_{Ht} + (e^{-\phi Z_t}-1)dN_{Ht}.
\label{eq:dividendprocess_model}
\end{equation}$$ We know from results in the previous sections, then, that the return on this stock satisfies an equation of the form $$\begin{equation}
dR_{St} = \left(F_t^{-1} + \mu_{St}\right)dt+ \sigma_{St}^{(\eta)}dB_{\eta t} + \sigma_{St}^{(H)}dB_{Ht} + (e^{-\zeta_{St}}-1)dN_{Ht},
\label{eq:stockreturn_model}
\end{equation}$$ where $F_t$ is the price-dividend ratio. Evidently, this claim cannot possibly be in positive supply, for we have already assumed that agents cannot invest in each other's capital. Thus, in equilibrium we will impose the condition that the net supply of this stock is zero.[^29]

## Consumption and investment 

To obtain equilibrium prices using the framework established in this paper, we must first determine the equilibrium consumption processes of individual agents, given the preferences and investment opportunities assumed in the model. The equations ([\[eq:idiocapitalprocess_model\]](#eq:idiocapitalprocess_model)) and ([\[eq:etaprocess_model\]](#eq:etaprocess_model)) imply a Markovian economic setting, meaning that agents' decisions can be obtained using a standard stochastic control approach. In this problem, agents choose human capital investment $x_{it}$, consumption $C_{it}$, and portfolio allocations to the bond and stock (described below), conditional on wealth $W_{it}$ and the idiosyncratic jump probability $\eta_t$. Wealth is defined as the sum of human capital $q_{it}H_{it}$ and financial wealth, the positions in the bond and stock.

### Return on human capital

In order to solve the consumption-investment problem of the agents, it will be most helpful to first determine the return on capital. As with any asset, this will depend on the dividend yield --- output, net of reinvestment, divided by the price $q_{it}$ --- and the capital gains rate: $$\begin{equation*}
dR_{Ht}^{(i)} = \underbrace{\frac{a-x_{it}}{q_{it}}dt}_{\textrm{dividend yield}} + \underbrace{\frac{d(q_{it}H_{it})}{q_{it^-}H_{it^-}}}_{\textrm{capital gains}}.
\label{eq:capitalreturn1_model}
\end{equation*}$$ In order to characterize these terms, we can conjecture and verify the dynamics of $q_{it}$. Foreseeing that agents will have constant consumption-wealth ratios and portfolio allocations, let us conjecture that $q_i$ is a constant.[^30] This conjecture implies that the capital gains rate $d(q_iH_{it})/(q_iH_{it^-})=dH_{it}/H_{it^-}$, and thus that the return on agent $i$'s human capital $$\begin{multline}
dR_{Ht}^{(i)} = \left(\frac{a-x_{it}}{q_i}+\Phi(x_{it})-\delta\right)dt+\sigma dB_{Ht} + (e^{-Z_t}-1)dN_{Ht}\\
+\tilde{\sigma} dB_{it} + (e^{-\tilde{Z}_t}-1)(dN_{it}-\eta_tdt).
\label{eq:capitalreturn2_model}
\end{multline}$$ Given this return, we know the dynamics of each agent's wealth.

### Consumption-savings decisions

Let $\alpha_{Ht}^{(i)}$ denote the share of wealth invested in capital --- that is, the value of human capital $q_iH_{it}$ as a fraction of total wealth $W_{it}$. Similarly, let $\alpha_{St}^{(i)}$ denote the share invested in the stock. It follows that agent $i$'s wealth evolves as $$\begin{equation*}
\frac{dW_{it}}{W_{it^-}} = \alpha_{Ht^-}^{(i)}dR_{Ht}^{(i)}+\alpha_{St^-}^{(i)}dR_{St}+(1-\alpha_{Ht^-}^{(i)}-\alpha_{St^-}^{(i)})r_tdt - \frac{C_{it}}{W_{it}}dt,
\label{eq:dwealth_model}
\end{equation*}$$ where the return on human capital $dR_{Ht}^{(i)}$ is given by ([\[eq:capitalreturn2_model\]](#eq:capitalreturn2_model)) and the return on the stock $dR_{St}$ is given by ([\[eq:stockreturn_model\]](#eq:stockreturn_model)). The agent's value function $V_{it}=J^{(i)}(W_{it},\eta_t)$ satisfies the HJB equation $$\begin{equation}
0 = \sup_{\left\{C_{it},x_{it},\alpha_{Ht}^{(i)},\alpha_{St}^{(i)}\right\}} \biggl\{ \bar{f}(C_{it},J^{(i)}(W_{it},\eta_t)) + \mathbb{E}_t[dJ^{(i)}(W_{it},\eta_t)] \biggr\}.
\label{eq:hjb_model}
\end{equation}$$ I write it out in full in Appendix equation ([\[eq:hjb_model_app\]](#eq:hjb_model_app)).

Solving for the equilibrium decisions requires taking the first-order conditions. First, consider the first-order condition with respect to investment: $$\begin{equation}
q_i = \Phi'(x_{it})^{-1} = \varphi x_{it} + 1.
\label{eq:focx_model}
\end{equation}$$ This is the standard q-theory result in a production economy. Notice that, when there are no adjustment costs ($\varphi=0$), $q=1$. Second, the first-order condition with respect to consumption is $$\begin{equation}
\rho(1-\gamma)\frac{J^{(i)}(W_{it},\eta_t)}{C_{it}} = J^{(i)}_W(W_{it},\eta_t).
\label{eq:foccons_model}
\end{equation}$$ This is the usual envelope condition: the marginal felicity of consumption equals the marginal value of wealth. Finally, the first-order conditions of the portfolio shares $\alpha_{Ht}^{(i)}$ and $\alpha_{St}^{(i)}$ (written out in ([\[eq:focalphah_model\]](#eq:focalphah_model)) and ([\[eq:focalphas_model\]](#eq:focalphas_model))) constitute the usual Merton result with intertemporal hedging, plus jump terms. These four conditions, together with the HJB equation ([\[eq:hjb_model\]](#eq:hjb_model)) and market clearing conditions, fully characterize the optimal consumption-savings decisions. The following proposition states the closed-form solution.

**Proposition 5**. *The value function of each agent $i\in\mathcal{I}$ takes the form $$\begin{equation}
J(w,\eta) = \frac{w^{1-\gamma}I(\eta)^{1-\gamma}}{1-\gamma},
\label{eq:valuefuncsol1_affine}
\end{equation}$$ where $$\begin{equation}
I(\eta)= \exp{\{a_I + b_I\eta\}}
\label{eq:valuefuncsol2_affine}
\end{equation}$$ for constants $$\begin{equation}
a_I = \frac{1}{\rho}\left(\Phi(x)-\delta + b_I\kappa_\eta\bar{\eta} - \frac{1}{2}\gamma(\sigma^2+\tilde{\sigma}^2) + \frac{1}{1-\gamma}\lambda \mathbb{E}_{\nu}[e^{-(1-\gamma)Z}-1] + \rho\log\rho\right).
\label{eq:valuecoeff_a_model}
\end{equation}$$ and $$\begin{equation}
b_I = \frac{\rho+\kappa_\eta}{(1-\gamma)\sigma_\eta^2} - \sqrt{\left(\frac{\rho+\kappa_\eta}{(1-\gamma)\sigma_\eta^2}\right)^2 - 2\frac{\mathbb{E}_{\tilde{\nu}}[e^{-(1-\gamma)\tilde{Z}}-1]+(1-\gamma)\mathbb{E}_{\tilde{\nu}}[1-e^{-\tilde{Z}}]}{(1-\gamma)^2\sigma_\eta^2}}.
\label{eq:valuecoeff_b_model}
\end{equation}$$ For each agent, the optimal portfolio allocations $\alpha_H=1$ and $\alpha_S=0$, optimal consumption $$C_{it}=\rho W_{it} = \rho qH_{it},$$ and the equilibrium human capital investment rate and price $$\begin{equation}
\bigl[x\quad q\bigr] = \biggl[ \frac{a-\rho}{1+\varphi \rho} \quad \frac{1+\varphi a}{1+\varphi \rho} \biggr].
\label{eq:investmentdecision_model}
\end{equation}$$*

The fact that agents' portfolios consist only of human capital is obviously unrealistic. However, this is merely a consequence of the assumption that it is the only positive-supply asset in the economy. One could easily add other positive-net-supply assets (like stocks, bonds, and physical capital) without changing the core asset pricing intuition. Likewise, the simplifying assumption of ex ante identical agents counterfactually implies identical portfolio allocations. Again, while this would matter if we were focused on matching portfolio-choice heterogeneity, it is not essential for the asset pricing quantities we are seeking.

## Equilibrium asset prices 

We have solved for optimal consumption and proven that it is proportional to the value of human capital. Thus, the consumption of each agent in this economy solves $$\begin{equation*}
\frac{dC_{it}}{C_{it^-}} = (\Phi(x)-\delta)dt + \underbrace{\sigma dB_{Ht} + (e^{-Z_t}-1)dN_{Ht}}_{\text{\rm endogenous systematic risk}} + \underbrace{\tilde{\sigma} dB_{it} + (e^{-\tilde{Z}_t}-1)(dN_{it} - \eta_{t}dt)}_{\text{\rm endogenous idiosyncratic risk}}.
\end{equation*}$$ This consumption process, together with identical isoelastic preferences and a square-root process for $\eta$, imply that this model is a case of what we have called the affine economy.[^31] Thus, we can apply the results of Appendix 8 to determine equilibrium asset prices.[^32]

[]

to .9 & & Parameter & & Value\
Panel A: Preferences\
Rate of time preference & & $\rho$ & &0.03\
Relative risk aversion & & $\gamma$ & &2.5\
Panel B: Aggregates\
Drift of aggregate consumption growth & & $\Phi(x)-\delta$ & &0.02\
Normal-times volatility of aggregate consumption growth & & $\sigma$ & &0.02\
Aggregate disaster distribution & & $(Z,\nu)$ & &\
Aggregate disaster probability & & $\lambda$ & &0.02\
Stock market leverage & & $\phi$ & &2\
Panel C: Idiosyncratic risks\
Normal-times volatility of idiosyncratic growth & & $\tilde{\sigma}$ & &0.1\
Idiosyncratic disaster distribution & & $(\tilde{Z}_i,\tilde{\nu})$ & & $N(0.1,0.2)$\
Average idiosyncratic disaster probability & & $\bar{\eta}$ & &0.04\
Mean-reversion of idiosyncratic disaster probability & & $\kappa_\eta$ & &0.065\
Volatility coefficient of idiosyncratic disaster probability & & $\sigma_\eta$ & &0.07\

\

Table [\[tab:calibtable\]](#tab:calibtable) summarizes the model calibration. The parameters governing preferences and macroeconomic aggregates take standard values in the literature, corresponding to U.S. data after World War II (henceforth, the post-war period). The parameters in Panel C, unique to the human-capital model, are chosen to match asset pricing moments in the data. More discussion on these choices follows in the result below.

### Riskfree rate

Equation ([\[eq:riskfreerate_thm_affine\]](#eq:riskfreerate_thm_affine)), the riskfree rate in the affine economy, implies that in this model $$\begin{equation}
r_t = \underbrace{\vphantom{\left(\bigl[(e^{\gamma\tilde{Z}_t}-1)(e^{-\tilde{Z}_t}-1)\bigr]\right)}\rho+\Phi(x)-\delta-\gamma\sigma^2 - \lambda \mathbb{E}_{\nu}\bigl[e^{\gamma Z}(1-e^{-Z})\bigr]}_{\textrm{standard complete-market model}} - \underbrace{\left(\gamma\tilde{\sigma}^2 + \eta_t\mathbb{E}_{\tilde{\nu}}\bigl[(e^{\gamma\tilde{Z}}-1)(1-e^{-\tilde{Z}})\bigr]\right)}_{\textrm{idiosyncratic risk}}.
\label{eq:riskfreerate_model}
\end{equation}$$ Figure 2 plots this interest rate in the calibrated model and compares it to the interest rate that would prevail in the complete-market version of this same economy.

<figure id="fig:riskfreerate" data-latex-placement="t">
<div class="center">
<img src="Calibration/Files/figures/riskfree" />
</div>
<figcaption>The figure shows the riskfree rate in the human-capital model as a function of the idiosyncratic disaster probability (solid line). The dashed line is the riskfree rate in a complete-market version of this economy, in which agents can trade claims to each other’s human capital.</figcaption>
</figure>

We can separate the riskfree rate into two components. The first is the riskfree rate that would prevail in a complete market; it is the standard result in a production economy with static disaster risk. Equivalently, it is the riskfree rate when a representative agent is endowed with aggregate capital $H_t=\int_\mathcal{I}H_{it}di$. The second component is the precautionary savings from uninsurable idiosyncratic risk, which strictly decreases the interest rate.

As in U.S. data, the model-implied riskfree rate is low. It is substantially lower than the interest rate that would prevail in a complete market, highlighting the importance of accounting for cross-sectional risks. Because I assume a normal-times consumption growth rate of approximately 2%, the level of this calibrated riskfree rate corresponds most closely to the post-2000 experience. Higher average output growth would allow the model to match the higher level of real interest rates in earlier periods like the 1980s.

The riskfree rate is also procyclical: it falls when the probability of an idiosyncratic disaster rises and equity prices fall (shown below). Still, it is relatively insensitive to changes in the idiosyncratic disaster intensity. Figure 2 shows that an increase of this state variable from 0% to 10% causes the riskfree rate to decline only about 1 percentage point.[^33] The next section shows that this sensitivity is much lower than the sensitivity of equity returns to the same changes. Thus, the model is consistent with historically low interest-rate volatility.

### Stock returns

As discussed in Appendix 8, it is easiest to price stocks in affine economies by separately pricing the *equity strips*. The $\tau$-maturity equity strip is the claim to the individual dividend $D_{t+\tau}$. The value of the total market is the sum of the equity strips over all $\tau\geq0$.

**Lemma 4**. *The equity strip with maturity $\tau$ has price $P_t^{(\tau)}=D_tG(\eta_t,\tau)$, where the price-dividend ratio $$\begin{equation}
G_t^{(\tau)}=\exp{\{a_G(\tau)+b_G(\tau)\eta_t\}}
\label{eq:equitystripprice_affine}
\end{equation}$$ for functions $$\begin{multline*}
a_G(\tau) = \biggl(- \rho +(\phi - 1)(\Phi(x) - \delta) + \gamma((1-\phi)\sigma^2+\tilde{\sigma}^2) +\lambda \mathbb{E}_{\nu}\left[e^{-(1-\gamma) Z}(e^{(1-\phi)Z}-1)\right]\\
+\frac{1}{2}\phi(\phi-1)\sigma^2 -\frac{\kappa_\eta\bar{\eta}}{\sigma_\eta^2}\left(\varpi_G+b_I\left(1-\gamma\right)\sigma_\eta^2 - \kappa_\eta\right)\biggr)\tau \\
-\frac{2\kappa_\eta\bar{\eta}}{\sigma_\eta^2}\log{\left(\frac{2\varpi_G-(\varpi_G+b_I\left(1-\gamma\right)\sigma_\eta^2 - \kappa_\eta)(1-e^{-\varpi_G\tau})}{2\varpi_G}\right)}
\end{multline*}$$ and $$\begin{equation*}
b_G(\tau) = -\frac{2\mathbb{E}_{\tilde{\nu}}\left[(e^{\gamma\tilde{Z}}-1)(1-e^{-\tilde{Z}})\right](1-e^{-\varpi_G\tau})}{2\varpi_G-(\varpi_G+b_I\left(1-\gamma\right)\sigma_\eta^2 - \kappa_\eta)(1-e^{-\varpi_G\tau})},
\end{equation*}$$ and constant $\varpi_G = \sqrt{(b_I\left(1-\gamma\right)\sigma_\eta^2 - \kappa_\eta)^2 + 2\mathbb{E}_{\tilde{\nu}}\left[(e^{\gamma\tilde{Z}}-1)(1-e^{-\tilde{Z}})\right]\sigma_\eta^2}$.*

This result gives us explicit equilibrium quantities for the stock's value $S_t=D_tF_t$, its price-dividend ratio $F_t=\int_0^\infty G_t^{(\tau)}d\tau$, and the coefficients governing its law of motion ([\[eq:stockreturn_model\]](#eq:stockreturn_model)). Specifically, the stock diffusion coefficients are $$\begin{equation*}
\sigma_S^{(H)} = \phi\sigma
\quad \textrm{and} \quad
\sigma_{St}^{(\eta)} = \frac{F_\eta(\eta_t)}{F(\eta_t)}\sigma_\eta\sqrt{\eta_t} =\left(\int_0^\infty\left(\frac{G_t^{(\tau)}}{\int_0^\infty G_t^{(\tau')}d\tau'}\right)b_G(\tau)d\tau\right)\sigma_\eta\sqrt{\eta_t},
\end{equation*}$$ and the stock price jump coefficient $\zeta_{St}=\phi Z_t$. While $\sigma_S^{(H)}$ and $\zeta_{St}$ depend only on systematic risk quantities, the term $\sigma_{St}^{(\eta)}$ comes entirely from cross-sectional risks $\eta$, even though these two risk sources are uncorrelated ($d[B_H,B_\eta]_t=0$).

<figure id="fig:stocks" data-latex-placement="t">
<div class="center">
<p><span>-2cm</span></p>
<table>
<tbody>
<tr>
<td style="text-align: center;"><strong>A. Volatility</strong></td>
<td style="text-align: center;"><strong>B. Risk premium</strong></td>
</tr>
<tr>
<td style="text-align: center;"><img src="Calibration/Files/figures/vol" alt="image" /></td>
<td style="text-align: center;"><img src="Calibration/Files/figures/prem" alt="image" /></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><strong>C. Sharpe ratio</strong></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="Calibration/Files/figures/sharpe" alt="image" /></td>
</tr>
</tbody>
</table>
</div>
<figcaption>The figure shows the conditional volatility (Panel A), risk premium (Panel B), and Sharpe ratio (Panel C) on the stock market in the human-capital model as a function of the idiosyncratic disaster probability (solid lines). The dashed lines represent these quantities in a complete-market version of this economy, in which agents can trade claims to each other’s human capital. Conditional volatility and the Sharpe ratio assume no aggregate jumps, because there were no aggregate consumption disasters in the U.S. post-war period.</figcaption>
</figure>

Panel A of Figure 3 plots the volatility of the stock, defined as the conditional standard deviation of its return:[^34] $$Volatility_t = \sqrt{d[R_S,R_S]_t} = \sqrt{\sigma_S^{(H)2}+\sigma_{St}^{(\eta)2}}.$$ Note that this is not the same as unconditional volatility, the standard deviation of returns over a given time interval. Unconditional volatility in this model will be larger, because it will also include the variance of expected returns, and expected returns vary with the idiosyncratic disaster probability. Regardless, the economics are clear from Figure 3: the human-capital model predicts high volatility, conditional and unconditional, of stock returns; this volatility rises in bad times. Thus, this model explains the high, countercyclical volatility of equity returns, resolving the "excess volatility\" puzzle (Shiller 1981).

The risk premium on this aggregate claim, then, equals $$\begin{equation}
r_{St}-r_t = \underbrace{\vphantom{\frac{F_\eta(\eta_t)}{F(\eta_t)}}\phi\gamma\sigma^2 + \lambda \mathbb{E}_{\nu}\left[(e^{\gamma Z}-1)(1-e^{-\phi Z})\right]}_{\text{\rm standard complete-market model}} + \underbrace{b_I(\gamma-1)\frac{F_\eta(\eta_t)}{F(\eta_t)}\sigma_\eta^2\eta_t}_{\text{\rm idiosyncratic risk}}.
\label{eq:riskpremiumthm_model}
\end{equation}$$ Panel B of Figure 3 plots this quantity. As with the riskfree rate, it has two components. The first is the standard complete-market, representative-agent result. Agents are compensated for the covariation of aggregate consumption and dividend shocks. We see that, even with large aggregate disasters, this premium is small. The second component is compensation for stochastic cross-sectional risk: time-varying cross-sectional disaster risk affects both marginal felicity ($\gamma>1/\psi=1$) and the stock's underlying volatility, generating a higher risk premium.

The risk premium at an idiosyncratic disaster probability of $\bar{\eta}=0.04$ is about 5--6%, consistent with historical data. The model thus resolves the classic equity premium puzzle (Mehra and Prescott 1985). Like equity volatility, the risk premium increases in idiosyncratic disaster risk. It is also far more sensitive to such increases than is the riskfree rate: an increase in the state variable from 0% to 10% causes the risk premium to increase by 8 percentage points (versus a 1 percentage point decline in the riskfree rate). The dominance of this risk-premium effect over the riskfree-rate effect means that the price-dividend ratio in the model is also procyclical, falling in bad times. In the next subsection, I confirm this claim using the historical time series of equity valuation ratios. The model then also explains return predictability: valuation ratios predict excess returns on stocks, despite low predictability of aggregate consumption and dividend growth (Cochrane 2008).

Finally, Panel C of Figure 3 shows the Sharpe ratio: the ratio of the stock market's risk premium to its volatility. While both the numerator and denominator of this quantity are increasing in the disaster probability, the numerator dominates, rendering the Sharpe ratio larger and countercyclical, as in the data.[^35]

## Does time-varying idiosyncratic risk drive asset prices? 

The human-capital model matches a multitude of asset pricing facts. But is this calibration consistent with the level and time-variation of cross-sectional income risk in the data? Because the model maps directly to moments in cross-sectional panel data, answering this question is relatively straightforward. This testability is an advantage over many leading explanations of asset pricing puzzles. For example, shows that a time-varying *aggregate* disaster probability can also explain many asset pricing phenomena; however, this story is based on a state variable that is difficult to estimate in data, especially at high frequencies, due to the rareness of such events.[^36] Cross-sectional disaster risk, in contrast, can be observed directly at the frequency of the panel data, since it is assumed that the ex ante probability should correspond closely to the distribution of ex post realizations.

The essential quantitative prediction of the model is that time-variation in cross-sectional income skewness, driven by changes in the idiosyncratic disaster intensity $\eta$, drives contemporaneous time-variation in asset pricing moments. There are two equivalent ways in which to test this. One could infer a time series $\{\hat{\eta}_t\}$ from cross-sectional income data and assess whether the implied time series of asset prices (e.g., price-dividend ratios) matches that in the data. One could alternatively infer $\{\hat{\eta}_t\}$ from asset prices and then assess the model-implied series of cross-sectional skewness. These are effectively the same test. Because the model is calibrated to match asset prices, I choose the latter approach.

<figure id="fig:timeseries" data-latex-placement="t">
<div class="center">
<table>
<tbody>
<tr>
<td style="text-align: center;"><strong>A. Idiosyncratic disaster risk</strong></td>
</tr>
<tr>
<td style="text-align: center;"><img src="Calibration/Files/figures/lamdata" alt="image" /></td>
</tr>
<tr>
<td style="text-align: center;"><strong>B. Cross-sectional income skewness</strong></td>
</tr>
<tr>
<td style="text-align: center;"><img src="Calibration/Files/figures/skewtimeseries" alt="image" /></td>
</tr>
</tbody>
</table>
</div>
<figcaption>The figure shows the time series of idiosyncratic disaster risk <span class="math inline"><em>η</em><sub><em>t</em></sub></span> (Panel A) and two-year cross-sectional income skewness (Panel B) implied by the history of monthly cyclically-adjusted price-earnings (CAPE) ratios on the U.S. stock market. Skewness is backward-looking: it is the skewness from year <span class="math inline"><em>t</em> − 2</span> to year <span class="math inline"><em>t</em></span>.</figcaption>
</figure>

To execute this test, I exploit the fact that the model implies a one-to-one mapping between the state variable $\eta_t$ and the price-dividend ratio on the stock market: $$\frac{S_t}{D_t} = \int_0^\infty\exp\left\{a_G(\tau)+b_G(\tau)\eta_t\right\}d\tau.$$ Using a time series of equity valuation ratios, one can invert this relation to infer an exact time series $\{\hat{\eta}_t\}$.[^37] For the equity valuation ratio, I use the cyclically-adjusted price-earnings (CAPE) ratio, detrended with a low-frequency filter to remove secular trends that are not captured by the model.[^38] The detrending is done so that the data capture business-cycle-frequency fluctuations in the series. Panel A of Figure 4 plots the implied time series of idiosyncratic disaster risk. The series confirms the earlier claim that, in recessions, cross-sectional risk rises and equity valuation ratios fall --- for instance, we see large peaks around the Great Depression and recent financial crisis.

From this asset-price-implied series $\{\hat{\eta}_t\}$, we can calculate an implied series of cross-sectional income skewness. The cross-sectional skewness over the time interval $[t-j,t]$ is $$Skewness_{\mathcal{I}}\left(\log{\frac{Y_{it}}{Y_{i,t-j}}}\right) = Skewness_{\mathcal{I}}\left(\tilde{\sigma}\int_{t-j}^tdB_{is} - \int_{t-j}^t\tilde{Z}_{is}dN_{is} + \int_{t-j}^t(1-e^{-\tilde{Z}_{is}})\eta_sds\right),$$ where $Skewness_{\mathcal{I}}(\cdot)$ yields the third central moment. The estimated series $\{\hat{\eta}_t\}$ implies a time series of these values for any given interval length $j$. Panel B of Figure 4 plots the model-implied two-year skewness over the full sample.[^39] The estimates are intuitive: cross-sectional income growth is left-skewed and cyclical (becomes more negative in bad times).

Now we can compare the model-implied cross-sectional skewness to the historical data. To do so, I use the large income dataset from the U.S. Social Security Administration (SSA), as summarized by . Figure 5 plots the cross-sectional skewness of income growth from these data over time. The series uses five-year income growth to capture the permanent component of income shocks.[^40] Along with these historical data, Figure 5 also plots the model-implied skewness from Panel B of Figure 4 above.

<figure id="fig:datavsmodel" data-latex-placement="t">
<div class="center">
<img src="Calibration/Files/figures/gosskewmodel" />
</div>
<figcaption>The figure compares the time series of cross-sectional skewness in the data (dotted line) to that implied by the model and historical equity valuation ratios (solid line). The data measure is the five-year skewness of income growth from Social Security Administration income data <span class="citation" data-cites="guvenan2014nature">(Guvenen et al. 2014)</span>. The model-implied skewness is exactly as in Panel B of Figure <a href="#fig:timeseries" data-reference-type="ref" data-reference="fig:timeseries">4</a>.</figcaption>
</figure>

Evidently, the two series are very close. This is a striking result, considering that all time-variation in the model-implied skewness series comes from time-variation in equity valuation ratios. This points to two conclusions. In the first place, a continuous-time model with an empirically realistic calibration can explain asset prices. Discrete time is not an essential condition. In the second place, uninsurable cross-sectional risk --- namely, cyclical skewness of shocks to human capital --- is an important driver of aggregate asset prices.

# Concluding remarks 

This paper has laid out a heterogeneous-agent framework which fully characterizes asset prices and has applied it to a parsimonious, quantitative model with inalienable human capital. The contributions of this paper are threefold. First, it unifies a disjoint literature on incomplete-market asset pricing, proving strong theoretical results about irrelevance and return dynamics. Second, the generalized framework subsumes a broad class of economic models, and may therefore be useful for applications in future work. Third, the paper presents compelling empirical evidence that time-varying cross-sectional skewness is a key determinant of asset pricing moments. In the rest of these concluding remarks, I address some lingering issues and discuss promising extensions of this paper.

The results of this paper bring to light a tension between discrete- and continuous-time models. One might dismiss this tension, asserting that one or the other timing assumption is simply inferior. Whether time is discrete or continuous is obviously a deeper question than I can address in these remarks. Regardless, I take the stance that it is less-than-ideal for the validity of an economic theory to operate under one time discretization and not the other.[^41]

The present study resolves this tension by showing that incomplete markets may still matter in continuous time, both in theory and in the data. In the human-capital model, non-separable preferences act as a way of preserving the economics without relying on a particular timing assumption. One might object to non-additive preferences; however, this may not be the only path to reconciliation. While a major contribution of this paper is the addition of Poisson jumps, infinite-variation Lévy jump processes can restore the conventional jump intuition (Protter 1992; Cont and Tankov 2004). My discussion of this possibility lays the groundwork for extending the results in my paper to the full set of Lévy processes.

Although the framework in this paper considers only asset prices, it is well-suited for addressing a broader set of macroeconomic questions. An emerging literature in macroeconomics explores the effects of heterogeneity and incomplete markets in continuous time. An overlapping literature studies the evolutions of the income and wealth distributions and their implications for macroeconomic quantities.[^42] In light of these papers, one sees how the heterogeneous-agent asset pricing framework in this paper presents a tractable way in which to jointly determine asset prices and other macroeconomic quantities in general equilibrium.

# Proofs of results in Section 2.2 

***Proof of Lemma 1**.* Equation ([\[eq:statepricedensity_theory\]](#eq:statepricedensity_theory)) follows directly from the results of . Note that, applying Itô's lemma to ([\[eq:statepricedensity_theory\]](#eq:statepricedensity_theory)), we get the law of motion $$\begin{multline}
\frac{d\pi_{it}}{\pi_{it^-}} = \mu_{\pi t}^{(i)}dt + \left(\frac{f_{CC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}\sigma_{Ct}^{(i)} + \frac{f_{CX,t}^{(i)}}{f_{Ct}^{(i)}}\sigma_{Xt}\right)^\top dB_t + \sum_{j=1}^n\left(\frac{f_C(C_{it^-}e^{-\zeta_{Ct}^{(i,j)}},X_{t^-}+\zeta_{Xt}^{(j)})}{f_C(C_{it^-},X_{t^-})}-1\right)dN_t^{(j)} \\
+ \frac{f_{CC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}\tilde{\sigma}_tdB_{it} +  \left(\frac{f_C(C_{it^-}e^{-\tilde{\zeta}_t},X_{t^-})}{f_C(C_{it^-},X_{t^-})}-1\right)dN_{it},
\label{eq:dpi1_theory}
\end{multline}$$ where subscripts denote partial derivatives of $f_C$ (e.g., $f_{CX}=\partial f_C/\partial X$), and where the drift term $$\begin{multline}
\mu_{\pi t}^{(i)} = f_{Vt}^{(i)}+\frac{f_{CC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}\left(\mu_{Ct}^{(i)}-\eta_t(e^{-\tilde{\zeta}_t}-1)\right) + \frac{f_{CX,t}^{(i)}}{f_{Ct}^{(i)}}\mu_{Xt} \\
+ \frac{1}{2}\frac{f_{CCC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}^2(|\sigma_{Ct}^{(i)}|^2 + \tilde{\sigma}_t^2) + \frac{1}{2}\frac{f_{CXX,t}^{(i)}}{f_{Ct}^{(i)}}|\sigma_{Xt}|^2 + \frac{f_{CCX,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}\sigma_{Ct}^{(i)\top}\sigma_{Xt}.
\label{eq:mupi_theory}
\end{multline}$$ For notational ease, we can rewrite ([\[eq:dpi1_theory\]](#eq:dpi1_theory)) as $$\frac{d\pi_{it}}{\pi_{it^-}} = \mu_{\pi t}^{(i)}dt + \sigma_{\pi t}^{(i)\top}dB_t + \sum_{j=1}^n(e^{\zeta_{\pi t}^{(i,j)}}-1)dN_t^{(j)} + \tilde{\sigma}_tdB_{it} + (e^{\tilde{\zeta}_{\pi t}^{(i)}}-1)dN_{it}$$ where the coefficients $\zeta_{\pi t}^{(i,j)}$ and $\tilde{\zeta}_{\pi t}^{(i)}$ are well-defined because $f_C$ is strictly positive.

We will prove the condition for the risk premium ([\[eq:riskpremium_general_theory\]](#eq:riskpremium_general_theory)) first, then show that it implies the condition for the riskfree rate ([\[eq:riskfreerate_general_theory\]](#eq:riskfreerate_general_theory)). By the assumption that all agents are unconstrained in their portfolio allocations, we have that, for any agent's state-price density process $\pi_i$, $$\begin{equation*}
S_t = \mathbb{E}_t\left[\int_t^\infty\frac{\pi_{is}}{\pi_{it}}D_sds\right].
\end{equation*}$$ The absence of arbitrage implies that this holds for any time $s>t$, so, after some algebraic manipulation, this expression implies $$\begin{equation*}
\pi_{it}S_t + \int_0^t\pi_{iu}D_udu = \mathbb{E}_t\left[\pi_{is}S_s+\int_0^s\pi_{iu}D_udu\right].
\end{equation*}$$ Therefore, $\pi_{it}S_t + \int_0^t\pi_{iu}D_udu$ is a martingale, and so it is a local martingale: $$\begin{equation*}
\mathbb{E}_t\left[d\left(\pi_{it}S_t\right)\right] + \pi_{it}D_tdt = 0.
\end{equation*}$$ Applying Itô's lemma, we can expand this as $$\begin{equation}
\mu_{St} + \mathbb{E}_{\tilde{\nu}}[\mu_{\pi t}^{(i)}] + \sigma_{\pi t}^{(i)\top}\sigma_{St} + \sum_{j=1}^n\lambda^{(j)}(e^{\zeta_{\pi t}^{(i,j)}-\zeta_{St}^{(j)}}-1) + \mathbb{E}_{\tilde{\nu}}\left[e^{\tilde{\zeta}_{\pi t}^{(i)}}-1\right] + \frac{D_t}{S_t} = 0,
\label{eq:stockeulermartingale_theory}
\end{equation}$$ which rearranges to $$\begin{multline*}
\underbrace{\frac{D_t}{S_t} + \mu_{St} + \sum_{j=1}^n\lambda^{(j)}(e^{-\zeta_{St}^{(j)}}-1)}_{r_{St}} + \underbrace{\mathbb{E}_{\tilde{\nu}}[\mu_{\pi t}^{(i)}] + \sum_{j=1}^n\lambda^{(j)}(e^{\zeta_{\pi t}^{(i,j)}}-1) + \mathbb{E}_{\tilde{\nu}}\left[e^{\tilde{\zeta}_{\pi t}^{(i)}}-1\right]}_{\mathbb{E}_t[d\pi_{it}/(\pi_{it^-}dt)]} \\
=\underbrace{- \sigma_{\pi t}^{(i)\top}\sigma_{St} + \sum_{j=1}^n\lambda^{(j)}\left[(e^{\zeta_{\pi t}^{(i,j)}}-1)(1-e^{-\zeta_{St}^{(j)}})\right]}_{-\mathbb{E}_t[d[\pi_i,R_S]_t/(\pi_{it^-}dt)]}.
\end{multline*}$$ All that remains, then, is to show ([\[eq:riskfreerate_general_theory\]](#eq:riskfreerate_general_theory)). To see this, one need only recognize that, letting $Q_t$ denote the price of the riskfree asset, $$\frac{dQ_t}{Q_t}=r_tdt.$$ This asset is like a stock with no dividends and no diffusion or jump terms, meaning that the arguments above all carry through with ([\[eq:stockeulermartingale_theory\]](#eq:stockeulermartingale_theory)) simplifying to $$r_t + \mathbb{E}_{\tilde{\nu}}[\mu_{\pi t}^{(i)}] + \sum_{j=1}^n\lambda^{(j)}(e^{\zeta_{\pi t}^{(i,j)}}-1) + \mathbb{E}_{\tilde{\nu}}\left[e^{\tilde{\zeta}_{\pi t}^{(i)}}-1\right] = 0,$$ which, of course, is equivalent to ([\[eq:riskfreerate_general_theory\]](#eq:riskfreerate_general_theory)). ◻

***Proof of Lemma 2**.* Let us begin the proof by conjecturing that the value function indeed takes the form ([\[eq:valuefuncconject_theory\]](#eq:valuefuncconject_theory)). In this case, we can evaluate each of the elasticities governing the state-price density process ([\[eq:dpi1_theory\]](#eq:dpi1_theory)). First, we have the coefficients of relative risk aversion $$-\frac{f_{CC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it} = \gamma.$$ Similarly, the coefficients of relative prudence are $$-\frac{f_{CCC,t}^{(i)}}{f_{CCt}^{(i)}}C_{it} = \gamma(\gamma+1).$$ Agents' *aversion to cross-sectional risk* also show up in the state-price density process, taking the form $$-\frac{f_{CX,t}^{(i)}}{f_{Ct}^{(i)}} = \left(\gamma-\frac{1}{\psi}\right)\frac{I_X(X_t)}{I(X_t)}.$$ This is a semi-elasticity of marginal felicity with respect to cross-sectional risk. It captures the percent increase in marginal felicity given a percent decline in $X$. We can likewise define the cross-elasticities $$-\frac{f_{CXX,t}^{(i)}}{f_{Ct}^{(i)}} = \left(\gamma-\frac{1}{\psi}\right)\left(\frac{I_{XX}(X_t)}{I(X_t)}-\left(\frac{I_X(X_t)}{I(X_t)}\right)^2\right)\quad\textrm{and}\quad -\frac{f_{CCX,t}^{(i)}}{f_{Ct}^{(i)}}C_{it} = -(\gamma+1)\left(\gamma-\frac{1}{\psi}\right)\frac{I_X(X_t)}{I(X_t)}.$$ Finally, the same mechanisms are embedded in the marginal felicity jumps from systematic and idiosyncratic jumps: $$\frac{f_C(C_{it^-}e^{-\zeta_C^{(i,j)}},X_{t^-}+\zeta_{Xt}^{(j)})}{f_C(C_{it^-},X_{t^-})} = e^{-\gamma\zeta_C^{(i,j)}}\left(\frac{I(X_{t^-}+\zeta_{Xt}^{(j)})}{I(X_{t^-})}\right)^{1/\psi-\gamma} \quad\textrm{and}\quad
\frac{f_C(C_{it^-}e^{-\tilde{\zeta}_t},X_{t^-})}{f_C(C_{it^-},X_{t^-})} = e^{-\gamma\tilde{\zeta}_t}.$$ For the purposes of this proof, the important fact about these expressions is that they are all identical across agents (with the exception of the marginal felicity jumps, which contain consumption growth interactions). Consequently, changes in state-price density ([\[eq:dpi1_theory\]](#eq:dpi1_theory)) become $$\begin{multline}
\frac{d\pi_{it}}{\pi_{it^-}} = \mu_{\pi t}^{(i)}dt - \left(\gamma\sigma_{Ct}^{(i)} + \left(\gamma-\frac{1}{\psi}\right)\frac{I_X(X_t)}{I(X_t)}\sigma_{Xt}\right)^\top dB_t \\
+ \sum_{j=1}^n\left(e^{\gamma\zeta_C^{(i,j)}}\left(\frac{I(X_{t^-}+\zeta_{Xt}^{(j)})}{I(X_{t^-})}\right)^{1/\psi-\gamma}-1\right)dN_t^{(j)} -\gamma\tilde{\sigma}_tdB_{it} +  \left(e^{\gamma\tilde{\zeta}_t}-1\right)dN_{it},
\label{eq:dpi2_theory}
\end{multline}$$ where $$\begin{multline*}
\mu_{\pi t}^{(i)} = f_V(X_t)-\gamma\left(\mu_{Ct}^{(i)}-\eta_t(e^{-\tilde{\zeta}_t}-1)\right) - \left(\gamma-\frac{1}{\psi}\right)\frac{I_X(X_t)}{I(X_t)}\mu_{Xt} + \frac{1}{2}\gamma^2(\gamma+1)(|\sigma_{Ct}^{(i)}|^2 + \tilde{\sigma}_t^2) \\
+ \frac{1}{2}\left(\gamma-\frac{1}{\psi}\right)\left(\left(\frac{I_X(X_t)}{I(X_t)}\right)^2-\frac{I_{XX}(X_t)}{I(X_t)}\right)|\sigma_{Xt}|^2 + (\gamma+1)\left(\gamma-\frac{1}{\psi}\right)\frac{I_X(X_t)}{I(X_t)}\sigma_{Ct}^{(i)\top}\sigma_{Xt}.
\end{multline*}$$ Aside from the idiosyncratic shocks $\{dB_i,dN_i\}$, these expressions differ across agents only by the coefficients $\{\mu_{Ct}^{(i)},\sigma_{Ct}^{(i)},\{\zeta_{Ct}^{(i,j)}\}_{j=1}^n\}$. The result that these coefficients must be equated across agents follows from the no-arbitrage conditions for the riskfree rate and risk premia --- ([\[eq:riskfreerate_general_theory\]](#eq:riskfreerate_general_theory)) and ([\[eq:riskpremium_general_theory\]](#eq:riskpremium_general_theory)), respectively. For each agent $i$, the excess return expressions ([\[eq:riskpremium_general_theory\]](#eq:riskpremium_general_theory)) constitute a system of $n+m$ linear equations in the $n+m$ coefficients $\{\sigma_{Ct}^{(i)},\{\exp\{-\gamma\zeta_{Ct}^{(i,j)}\}\}_{j=1}^n\}$. These equations are, by assumption, non-redundant, so the solution to this system must satisfy $\{\sigma_{Ct}^{(i)},\{\zeta_{Ct}^{(i,j)}\}_{j=1}^n\}=\{\sigma_{Ct}^{(i')},\{\zeta_{Ct}^{(i',j)}\}_{j=1}^n\}$ for all $(i,i')\in\mathcal{I}\times\mathcal{I}$. Since coefficients must be equated across agents, imposing goods-market clearing $\int_\mathcal{I}C_{it}di=C_t$ implies that $\{\sigma_{Ct}^{(i)},\{\zeta_{Ct}^{(i,j)}\}_{j=1}^n\}=\{\sigma_C,\{\zeta_C^{(j)}\}_{j=1}^n\}$. Given this fact, the riskfree rate ([\[eq:riskfreerate_general_theory\]](#eq:riskfreerate_general_theory)) becomes affine in $\mu_{Ct}^{(i)}$ for each agent. Identical argumentation then implies that $\mu_{Ct}^{(i)}=\mu_C$ for all $i\in\mathcal{I}$. This proves the claim in the first part of the lemma.

To complete the proof, we must verify that $J(C_{it},X_i)$ takes the conjectured form. By definition, we have $$J(C_{it},X_t) = \mathbb{E}_t\left[\int_t^\infty\bar{f}(C_{is},X_s)ds\right].$$ As we did in the proof of Lemma 1, we can rearrange this with some algebra to get that, for all $s>t$, $$J(C_{it},X_t) + \int_0^t\bar{f}(C_{iu},X_u)du = \mathbb{E}_t\left[J(C_{is},X_s) + \int_0^s\bar{f}(C_{iu},X_u)du\right].$$ The left-hand side of this is therefore a martingale, and so it must be that $$\mathbb{E}_t[dJ(C_{it},X_t)] + \bar{f}(C_{it},X_t) = 0.$$ This is the usual HJB equation. Applying Itô's lemma, this HJB equation expands to the partial differential equation $$\begin{multline}
0 = J_Cc\left(\mu_C - \eta(x)\mathbb{E}_{\tilde{\nu}}\left[e^{-\tilde{\zeta}(x,\tilde{Z}_t)}-1\right]\right) + J_X\mu_X(x) \\
+ \frac{1}{2}J_{CC}c^2\left(|\sigma_C|^2 + \tilde{\sigma}(x)^2\right) + \frac{1}{2}J_{XX}|\sigma_X(x)|^2 + J_{CX}c\sigma_C^\top\sigma_X(x) \\
+ \sum_{j=1}^n\lambda^{(j)}\left[J(ce^{-\zeta_C^{(j)}},x+\zeta_{X}^{(j)}(x))-J(c,x)\right] \\
+ \eta(x)\mathbb{E}_{\tilde{\nu}}\left[J(ce^{-\tilde{\zeta}(x,\tilde{Z})},x)-J(c,x)\right] + \bar{f}(c,J(c,x)).
\end{multline}$$ Substituting in the conjecture ([\[eq:valuefuncconject_theory\]](#eq:valuefuncconject_theory)) and dividing by $c^{1-\gamma}I(x)^{1-\gamma}$ gives us the ODE $$\begin{multline}
0 = \mu_C - \eta(x)\mathbb{E}_{\tilde{\nu}}\left[e^{-\tilde{\zeta}(x,\tilde{Z})}-1\right] - \frac{1}{2}\gamma \left(|\sigma_C|^2 + \tilde{\sigma}(x)^2\right)+\frac{I_X(x)}{I(x)}(\mu_X(x)+(1-\gamma)\sigma_C^\top\sigma_X(x))  \\
-\frac{1}{2}\left(\gamma \frac{I_{X}(x)^2}{I(x)^2} - \frac{I_{XX}(x)}{I(x)}\right)|\sigma_X(x)|^2 + \eta(x)\frac{1}{1-\gamma}\mathbb{E}_{\tilde{\nu}}\left[e^{-(1-\gamma)\tilde{\zeta}(x,\tilde{Z})}-1\right]\\
+ \sum_{j=1}^n\lambda^{(j)}\frac{1}{1-\gamma}\left[e^{-(1-\gamma)\zeta_C^{(j)}}\left(\frac{I(x+\zeta_{X}^{(j)}(x))}{I(x)}\right)^{1-\gamma}-1\right] + \hat{f}(x),
\label{eq:hjbconject_theory}
\end{multline}$$ for $$\begin{equation}
\hat{f}(x)=\frac{\bar{f}(c,J(c,x))}{c^{1-\gamma}I(x)^{1-\gamma}} = \begin{cases}
\dfrac{\rho}{1-1/\psi}\left(I(x)^{1/\psi-1}-1\right) &\textrm{if}\quad \psi\neq1, \\
-\rho\log{I(x)} &\textrm{if}\quad \psi=1.
\end{cases}
\end{equation}$$ This verifies the conjecture and determines the solution to $I(x)$. ◻

***Proof of Lemma 3**.* By the assumption that all agents are unconstrained in their portfolio allocations, we have that, for any agent's state-price density process $\pi_i$, $$\begin{equation}
S_t = \mathbb{E}_t\left[\int_t^\infty\frac{\pi_{is}}{\pi_{it}}D_sds\right].
\label{eq:equitystripeuler_theory}
\end{equation}$$ Moreover, for all $s>t$, the solution to the stochastic differential equation ([\[eq:ddividend_setup\]](#eq:ddividend_setup)) can be written as $$\begin{align*}
D_s &=D_te^{\int_t^s\left(\mu_D-\frac{1}{2}|\sigma_D|^2\right)du + \int_t^s\sigma_D^\top dB_u - \sum_{j=1}^n\int_t^s\zeta_D^{(j)}dN_u^{(j)}}\\
&=D_tL(\{B_u,N_u^{(j)}:u\in[t,s],j\in\{1,\dots,n\}\}).
\end{align*}$$ In words, the future dividend $D_s$ can be expressed as the product of the current dividend $D_t$ and some function $L$ that is independent of $D$. (The same is true if we allow the coefficients $\mu_D$, $\sigma_D$ and $\zeta_D^{(j)}$ to be functions of $X$.) We have shown in the proof of Lemma 2 that the state-price density term $\pi_{is}/\pi_{it}$ is a function of $X$ over horizon $[t,s]$. Hence, using the fact that all of these variables are Markovian, the expectation in ([\[eq:equitystripeuler_theory\]](#eq:equitystripeuler_theory)) must evaluate to $$S_t = D_tF(X_t),$$ for some function $F$, as claimed. Now, applying Itô's lemma to this price process, it follows that the deterministic drift coefficient $$\begin{equation}
\mu_{St} = \mu_{D} + \frac{F_{Xt}}{F_t}\mu_{Xt} + \frac{1}{2}\frac{F_{XX,t}}{F_t}|\sigma_{Xt}|^2 + \frac{F_{Xt}}{F_t}\sigma_{D}^\top\sigma_{Xt},
\label{eq:equitydrift_theory}
\end{equation}$$ and the diffusion and jump coefficients equal those stated in the lemma.

To characterize the solution $F$, we need only apply the equilibrium return relations ([\[eq:riskfreerate_general_theory\]](#eq:riskfreerate_general_theory)) and ([\[eq:riskpremium_general_theory\]](#eq:riskpremium_general_theory)). Because we have proven that $S_t$ solves a stochastic differential equation of the form ([\[eq:dstockprice_theory\]](#eq:dstockprice_theory)), we can apply Lemma 2 and use the fact that each $\pi_i$ solves ([\[eq:dpi2_theory\]](#eq:dpi2_theory)). It follows that $F$ solves the differential equation $$\begin{multline}
\underbrace{F(x)^{-1} - \mu_S(x) + \sum_{j=1}^n\lambda^{(j)}(e^{-\zeta_S^{(j)}(x)}-1)}_{r_S(x)} - r(x) = \left(\gamma\sigma_C + \left(\gamma-\frac{1}{\psi}\right)\frac{I_X(x)}{I(x)}\sigma_X(x)\right)^\top\sigma_S(x) \\
+ \sum_{j=1}^n\lambda^{(j)}\left[\left(e^{\gamma\zeta_C^{(j)}}\left(\frac{I(x+\zeta_X^{(j)}(x))}{I(x)}\right)^{1/\psi-\gamma}-1\right)\left(1-e^{-\zeta_S^{(j)}(x)}\right)\right],
\label{eq:equitypde_theory}
\end{multline}$$ where the stock-return coefficients $\mu_S(x)$, $\sigma_S(x)$, and $\zeta_S^{(j)}(x)$ are defined above, and the interest rate $r(x)$ is stated explicitly later in the paper. ◻

# Proofs of results in Section 2.3 

***Proofs of Propositions 1 and 2**.* Suppose $\pi_i^{\rm CM}=\pi_{i'}^{\rm CM}$, almost surely, for all agents $i$ and $i'$. Then each of the coefficients in the equation ([\[eq:dpi2_theory\]](#eq:dpi2_theory)) must be equated across agents. Because we have assumed that $d[B_i,B_{i'}]_t=d[N_i,N_{i'}]_t=0$ for all $i\neq i'$, and because $f_{Ct}^{(i)}/f_{CC,t}^{(i)}$ is strictly non-zero, it must be that, almost surely, $\tilde{\sigma}(X_t)=0$ and $\eta(X_t)\tilde{\zeta}(X_t,\tilde{Z}_t)=0$. The state-price density process ([\[eq:dpi2_theory\]](#eq:dpi2_theory)) simplifies to $$\begin{equation}
\frac{d\pi_{it}^{\rm CM}}{\pi_{it^-}^{\rm CM}} = \left(f_V -\gamma\mu_C + \frac{1}{2}\gamma^2(\gamma+1)|\sigma_C|^2 \right)dt - \gamma\sigma_C^\top dB_t + \sum_{j=1}^n\left(e^{\gamma\zeta_C^{(j)}}-1\right)dN_t^{(j)}.
\label{eq:dstatepricedensity_cm_theory}
\end{equation}$$ Setting $\tilde{\sigma}(x)=\eta(x)\tilde{\zeta}(x,\tilde{Z})=0$ in the ODE ([\[eq:hjbconject_theory\]](#eq:hjbconject_theory)), we also get that $I(x)$ equals some constant $I$. Consequently, the ODE ([\[eq:equitypde_theory\]](#eq:equitypde_theory)) implies that the price-dividend ratio $F(x)$ reduces to a constant $F$; thus, the equity-risk coefficients are as stated in Proposition 2.

By these results, it suffices to solve for the riskfree rate and risk premia in the incomplete market and then evaluate it in the complete market by setting $\tilde{\sigma}(x)=\eta(x)\tilde{\zeta}(x,\tilde{Z})=0$, $I(x)=I$, and $F(x)=F$. The proofs of these incomplete-market returns are completed below. ◻

***Proof of Proposition 3**.* Substituting the state-price density process ([\[eq:dpi2_theory\]](#eq:dpi2_theory)) (with the proper consumption-growth coefficients) into the riskfree rate expression from Lemma 1 implies $$\begin{multline}
r_t =  -f_V(X_t) + \gamma\mu_C - \frac{1}{2}\gamma(\gamma+1)(|\sigma_C|^2+\tilde{\sigma}(X_t)^2) - \left(\frac{1}{\psi}-\gamma\right)\frac{I_X(X_t)}{I(X_t)}\left(\mu_X(X_t) - (1-\gamma)\sigma_C^\top\sigma_X(X_t)\right) \\
- \frac{1}{2}\left(\frac{1}{\psi}-\gamma\right)\left(\frac{I_{XX}(X_t)}{I(X_t)}+\left(\frac{1}{\psi}-\gamma-1\right)\frac{I_{X}(X_t)^2}{I(X_t)^2}\right)|\sigma_X(X_t)|^2 \\
-\sum_{j=1}^n\lambda^{(j)}\left[e^{\gamma\zeta_C^{(j)}}\left(\frac{I(X_t+\zeta_{Xt}^{(j)})}{I(X_t)}\right)^{1-\gamma} - 1\right] - \eta_t\mathbb{E}_{\tilde{\nu}}\left[e^{\gamma\tilde{\zeta}_t}-1+\gamma(e^{-\tilde{\zeta}_t}-1)\right].
\label{eq:riskfree_withfv}
\end{multline}$$ For the sake of both mathematical simplicity and economic intuition, it is useful to derive an equivalent expression for $f_{Vt}$ in terms of exogenous values. Note first that $$\begin{equation*}
f_V(x) = -\rho - \left(\gamma-\frac{1}{\psi}\right)\dfrac{\rho}{1-1/\psi}(I(x)^{1/\psi-1}-1).
\end{equation*}$$ Second, rearranging the ODE ([\[eq:hjbconject_theory\]](#eq:hjbconject_theory)) for $I(x)$, we have that $$\begin{multline}
-\frac{\rho}{1-1/\psi}\left(I(x)^{1/\psi-1}-1\right) = \mu_C  + \frac{I_X(x)}{I(x)}\mu_X(x) - \frac{1}{2}\gamma \left(|\sigma_C|^2 + \tilde{\sigma}(x)^2\right) \\
-\frac{1}{2}\left(\gamma \frac{I_{X}(x)^2}{I(x)^2} - \frac{I_{XX}(x)}{I(x)}\right)|\sigma_X(x)|^2 + (1-\gamma)\frac{I_X(x)}{I(x)}\sigma_C^\top\sigma_X(x) \\
+ \sum_{j=1}^n\lambda^{(j)}\frac{1}{1-\gamma}\left[e^{-(1-\gamma)\zeta_C^{(j)}}\left(\frac{I(x+\zeta_{X}^{(j)}(x))}{I(x)}\right)^{1-\gamma}-1\right] \\
+ \eta(x)\frac{1}{1-\gamma}\mathbb{E}_{\tilde{\nu}}\left[e^{-(1-\gamma)\tilde{\zeta}(x,\tilde{Z})}-(1-\gamma)e^{-\tilde{\zeta}(x,\tilde{Z})}-\gamma\right].
\end{multline}$$ Combining these facts implies that the marginal felicity of value is equal to $$\begin{multline}
f_V(x) = - \rho - \left(\frac{1}{\psi}-\gamma\right)\biggl(\mu_C  + \frac{I_X(x)}{I(x)}\mu_X(x) - \frac{1}{2}\gamma \left(|\sigma_C|^2 + \tilde{\sigma}(x)^2\right) \\
-\frac{1}{2}\left(\gamma \frac{I_{X}(x)^2}{I(x)^2} - \frac{I_{XX}(x)}{I(x)}\right)|\sigma_X(x)|^2 + (1-\gamma)\frac{I_X(x)}{I(x)}\sigma_C^\top\sigma_X(x) \\
+ \sum_{j=1}^n\lambda^{(j)}\frac{1}{1-\gamma}\left[e^{-(1-\gamma)\zeta_C^{(j)}}\left(\frac{I(x+\zeta_{X}^{(j)}(x))}{I(x)}\right)^{1-\gamma}-1\right] \\
+ \eta(x)\frac{1}{1-\gamma}\mathbb{E}_{\tilde{\nu}}\left[e^{-(1-\gamma)\tilde{\zeta}(x,\tilde{Z})}-1-(1-\gamma)(e^{-\tilde{\zeta}(x,\tilde{Z})}-1)\right]\biggr).
\label{eq:sdudrift_special}
\end{multline}$$ Now we can substitute in the expression ([\[eq:sdudrift_special\]](#eq:sdudrift_special)) for $f_V(X_t)$ into ([\[eq:riskfree_withfv\]](#eq:riskfree_withfv)) to get the riskfree rate expression stated in the proposition. ◻

***Proof of Proposition 4**.* The expression follows simply from substituting the state-price density process ([\[eq:dpi2_theory\]](#eq:dpi2_theory)) (with the proper consumption-growth coefficients) into the risk premium expression from Lemma 1. ◻

# Proofs of results in Section 2.4 

***Proof of Theorem 1**.* That these two conditions together are sufficient for relevance follows from the risk premium expression ([\[eq:riskpremiumthm1_theory\]](#eq:riskpremiumthm1_theory)). Since preferences are non-additive, $\gamma\neq1/\psi$; since cross-sectional risk is stochastic, $I_X(x)/I(x)\neq0$ and $I(x+\zeta_X)/I(x)\neq1$. Thus, because shocks to cross-sectional risks are correlated with shocks to equity returns, either $\sigma_X^\top\sigma_S\neq0$ or $\zeta_X^{(j)}\zeta_S^{(j)}\neq0$ for some $j$. If $\sigma_X^\top\sigma_S\neq0$, then the Brownian term is strictly non-zero; if $\zeta_X^{(j)}\zeta_S^{(j)}\neq0$ for the $j$th jump, then the premium term for that jump is strictly different from the corresponding complete-market term in ([\[eq:riskpremium_cm_theory\]](#eq:riskpremium_cm_theory)).

To see sufficiency, consider what happens to risk premia if either condition does not hold. Suppose shocks to cross-sectional risks are uncorrelated with shocks to equity returns: $\sigma_X^\top\sigma_S=\zeta_X^{(j)}\zeta_S^{(j)}=0$ for all $j$. Because $\sigma_X^\top\sigma_S=0$, the Brownian risk-premium term disappears. If $\zeta_X^{(j)}\zeta_S^{(j)}\neq0$, then all jump terms collapse to their complete-market counterparts: either $\zeta_X^{(j)}=\zeta_S^{(j)}=0$; or $\zeta_X^{(j)}=0$ when $\zeta_S^{(j)}\neq0$, so that $I(x+\zeta_X^{(j)})/I(x)=1$; or $\zeta_S^{(j)}=0$ when $\zeta_X^{(j)}\neq0$, so the entire term is zero in both the incomplete- and complete-market economies. This proves that cross-sectional risk must be correlated with equity risks, no matter what form preferences take.

Now suppose agents have time-additive power utility: $\gamma=1/\psi$. Clearly, the risk premia expressions ([\[eq:riskpremiumthm1_theory\]](#eq:riskpremiumthm1_theory)) and ([\[eq:riskpremium_cm_theory\]](#eq:riskpremium_cm_theory)) become identical. Thus, non-additive utility is also necessary for relevance. ◻

***Proof of Theorem 2**.* Before establishing the necessity and sufficiency of this conditions, let us consider the implications of stochasticity in cross-sectional risk for equity risks. Recall that the general-equilibrium stock price coefficients are $$\begin{equation*}
\sigma_{St} = \sigma_{D} + \frac{F_{Xt}}{F_t}\sigma_{Xt}
\quad\textrm{and}\quad 
e^{-\zeta_{St}^{(j)}} = e^{-\zeta_{D}^{(j)}}\frac{F(X_{t^-}+\zeta_{Xt}^{(j)})}{F(X_{t^-})}.
\end{equation*}$$ They differ from those in the complete market if and only if $F$ depends on $X$. Recognize also that, whenever $X$ is time-varying, the riskfree rate $r$ is a function of $X$ in the incomplete-market economy. Thus, from the differential equation ([\[eq:equitypde_theory\]](#eq:equitypde_theory)), we can conclude that the price-dividend ratio $F$ is a function of $X$ if and only if $X$ is time-varying. As a result, these stock price coefficients depend on $\sigma_{Xt}$ and $\zeta_{Xt}^{(j)}$, and it must be that $X$ is correlated with the stock: either $\sigma_{Xt}^\top\sigma_{St}\neq0$, $\zeta_{Xt}^{(j)}\zeta_{St}^{(j)}\neq0$ for some $j$, or multiple of these. In the complete-market economy, however, $F$ is independent of $X$, and thus so are the stock coefficients. In summary, saying that cross-sectional risk is stochastic is equivalent to saying that it is stochastic and correlated with the stock (condition 1 from Theorem 1).

Now let us establish that these conditions are sufficient for relevance. Suppose cross-sectional risk is stochastic (condition 1) and felicity is non-additive (condition 2(a)). The sufficiency of these conditions follows from Theorem 1, since cross-sectional risk is stochastic and correlated with the stock. Now suppose, alternatively, that cross-sectional risk is stochastic (condition 1) and correlated with aggregate consumption growth (condition 2(b)). In mathematical terms, this means $\sigma_C^\top\sigma_{Xt}\neq0$, $\zeta_C^{(j)}\zeta_{Xt}^{(j)}\neq0$ for some $j$, or multiple of these. If $\sigma_C^\top\sigma_{Xt}\neq0$, then the incomplete-market risk premium has a nonzero term $\gamma\sigma_C^\top\sigma_{Xt}\neq0$ that is not present in the complete market. Similarly, if $\zeta_C^{(j)}\zeta_{Xt}^{(j)}\neq0$ for some $j$, then the $j$th jump term in the risk premium expression must be strictly different from that in the complete market. Specifically, if $\gamma=1/\psi$, then this term becomes $$\lambda^{(j)}\left[\left(e^{\gamma\zeta_C^{(j)}}-1\right)\left(1-e^{-\zeta_D^{(j)}}\frac{F(X_{t^-}+\zeta_{Xt}^{(j)})}{F(X_{t^-})}\right)\right],$$ which is strictly different from the corresponding complete-market term because $\zeta_C^{(j)}$ and $\zeta_{Xt}^{(j)}$ are strictly non-zero and, in turn, $F(x+\zeta_X^{(j)})/F(x)\neq1$. Thus, conditions 1 and 2(b) are sufficient for relevance.

The necessity of stochastic cross-sectional risk (condition 1) follows from the arguments above and in the proof of Theorem 1. If it is non-stochastic, then the equity-risk coefficients $\sigma_S$ and $\zeta_S^{(j)}$ are the same in the complete- and incomplete-market economies. Moreover, if cross-sectional risk is non-stochastic, then it is certainly not correlated with equity risk. Thus, by Theorem 1, risk premia are unaffected by market incompleteness (regardless of preferences), proving that this condition is essential.

Finally, let us show the necessity of at least one of conditions 2(a) and 2(b) holding. Suppose neither holds: $\gamma=1/\psi$ and $\sigma_C^\top\sigma_X=\zeta_C^{(j)}\zeta_{Xt}^{(j)}=0$ for all $j$. Then the equity-risk coefficients are the same as in the complete market, and the risk premium expression ([\[eq:riskpremiumthm1_theory\]](#eq:riskpremiumthm1_theory)) and ([\[eq:riskpremium_cm_theory\]](#eq:riskpremium_cm_theory)) become identical. Thus, it is necessary that at least one of these hold. ◻

# Details of the affine economy from Section 2.6 

This section lays out the affine economy discussed in Section 2.6 and used in Section 3 of the main text. This section makes two generalizations to the main framework from the paper. First, it allows jump-risk coefficients $\zeta$ to be functions of random variables $Z$. This is just to map the framework to the human-capital model in Section 3. Second, it allows dividend-growth coefficients $\mu_D$, $\sigma_D$ and $\zeta_D^{(j)}$ be (affine) functions of the state variable $X$. The defining assumption of the affine economy is as follows.

**Assumption 7** (Affine coefficients). *The coefficients above take the explicit form $$\begin{tabular}{ccc}
$\begin{aligned}[c]
\mu_X(x) &= \bar{\mu}_X^{(0)} + \bar{\mu}_X^{(1)}x \\
|\sigma_X(x)|^2 &= \bar{\sigma}_X^{(0)} + \bar{\sigma}_X^{(1)}x \\
\zeta_X(x,Z_X^{(j)}) &= Z_X^{(j)} \\
\tilde{\sigma}(x)^2 &= \bar{\tilde{\sigma}}^{(0)} + \bar{\tilde{\sigma}}^{(1)}x \\
\tilde{\zeta}(x,\tilde{Z}) &= \tilde{Z}
\end{aligned}$ & \hspace{1cm} &
$\begin{aligned}[c]
\eta(x) &= \bar{\eta}^{(0)} + \bar{\eta}^{(1)}x \\
\mu_D(x) &= \bar{\mu}_D^{(0)} + \bar{\mu}_D^{(1)}x \\
\zeta_D(x,Z_D^{(j)}) &= Z_D^{(j)} \\
\sigma_X(x)^\top\sigma_D(x) &= \bar{\sigma}_{XD}^{(0)} + \bar{\sigma}_{XD}^{(1)}x \\
\sigma_C^\top\sigma_D(x) &= \bar{\sigma}_{CD}^{(0)} + \bar{\sigma}_{CD}^{(1)}x,
\end{aligned}$\\
\end{tabular}$$ where all of the scalars satisfy the conditions specified in Section 2.1. Furthermore, the Brownian shocks to aggregate consumption growth and cross-sectional risk are uncorrelated: $\sigma_C^\top\sigma_{Xt}=0$ almost surely.*

We will henceforth refer to the special case of the isoelastic economy in which this assumption holds as the *affine economy*. Notice that Assumption 7 represents an approximation of the full isoelastic economy if we take first-order Taylor expansions of the true coefficients, so long as $\sigma_C^\top\sigma_{Xt}=0$ and the jump magnitudes $\zeta_X$ and $\tilde{\zeta}$ do not depend on $X$. The reason the affine economy is of interest is that it yields fully explicit solutions for the value functions and, in turn, asset prices and returns.[^43]

**Proposition 6** (Value function). *The value function of each agent $i\in\mathcal{I}$ takes the form ([\[eq:valuefuncconject_theory\]](#eq:valuefuncconject_theory)) with $$\begin{equation}
I(x)\approx \exp{\{a_I + b_Ix\}},
\label{eq:valuefuncsol_affine}
\end{equation}$$ where the constants $$\begin{multline}
a_I = \frac{1}{k_0}\biggl(\frac{1}{1-1/\psi}(k_0\log{\rho}+k_1-\rho)+\mu_C + b_I\bar{\mu}_X^{(0)} \\
- \frac{1}{2}\gamma \left(|\sigma_C|^2 + \bar{\tilde{\sigma}}^{(0)}\right) -\frac{1}{2}b_I^2\left(\gamma-1\right)\bar{\sigma}_X^{(0)} + \sum_{j=1}^n\lambda^{(j)}\frac{1}{1-\gamma}\mathbb{E}_{\nu_{CX}^{(j)}}\left[e^{-(1-\gamma)(Z_C^{(j)}-b_IZ_X^{(j)})}-1\right] \\
+ \bar{\eta}^{(0)}\frac{1}{1-\gamma}\mathbb{E}_{\tilde{\nu}}\left[e^{-(1-\gamma)\tilde{Z}}-1-(1-\gamma)(e^{-\tilde{Z}}-1)\right]\biggr),
\label{eq:valuecoeff_a_affine}
\end{multline}$$ and $$\begin{equation}
b_I = \frac{k_0-\bar{\mu}_X^{(1)}}{\left(1-\gamma\right)\bar{\sigma}_X^{(1)}} -\sqrt{\left(\frac{k_0-\bar{\mu}_X^{(1)}}{\left(1-\gamma\right)\bar{\sigma}_X^{(1)}}\right)^2+2\frac{\gamma(1-\gamma)\bar{\tilde{\sigma}}^{(1)}-\bar{\eta}^{(1)}\mathbb{E}_{\tilde{\nu}}\left[e^{-\tilde{Z}}(e^{\gamma\tilde{Z}}-1) + \gamma(e^{-\tilde{Z}}-1)\right]}{\left(1-\gamma\right)^2\bar{\sigma}_X^{(1)}}}.
\label{eq:valuecoeff_b_affine}
\end{equation}$$ for $k_0=\exp{\left\{\log{\rho}+\left(1/\psi-1\right)(a_I+b_I\mathbb{E}[x])\right\}}$ and $k_1=k_0(1-\log{k_0})$.*

*When $\psi=1$, the solution ([\[eq:valuefuncsol_affine\]](#eq:valuefuncsol_affine)) is exact and the system of equations ([\[eq:valuecoeff_a_affine\]](#eq:valuecoeff_a_affine)) and ([\[eq:valuecoeff_b_affine\]](#eq:valuecoeff_b_affine)) continues to hold with $\lim_{\psi\to1}k_0=\rho$ and $\lim_{\psi\to1}(k_0\log{\rho}+k_1-\rho)/(1-1/\psi)=0$.*

***Proof of Proposition 6**.* Conjecture that $I(x)$ is exponential affine in $x$, as in ([\[eq:valuefuncsol_affine\]](#eq:valuefuncsol_affine)). Suppose first that $\psi\neq1$. Given this conjecture and our assumption of affine coefficients, the ODE ([\[eq:hjbconject_special\]](#eq:hjbconject_special)) from Proposition [\[prop:valuefunc_special\]](#prop:valuefunc_special) becomes $$\begin{multline}
0 = \mu_C + (\bar{\eta}^{(0)} + \bar{\eta}^{(1)}x)\mathbb{E}_{\tilde{\nu}}\left[1-e^{-\tilde{Z}}\right] + b_I(\bar{\mu}_X^{(0)} + \bar{\mu}_X^{(1)}x) - \frac{1}{2}\gamma \left(|\sigma_C|^2 + \bar{\tilde{\sigma}}^{(0)} + \bar{\tilde{\sigma}}^{(1)}x\right) \\
-\frac{1}{2}b_I^2\left(\gamma-1\right)(\bar{\sigma}_X^{(0)} + \bar{\sigma}_X^{(1)}x) + \sum_{j=1}^n\lambda^{(j)}\frac{1}{1-\gamma}\mathbb{E}_{\nu_{CX}^{(j)}}\left[e^{-(1-\gamma)(Z_C^{(j)}-b_IZ_X^{(j)})}-1\right] \\
+ (\bar{\eta}^{(0)} + \bar{\eta}^{(1)}x)\frac{1}{1-\gamma}\mathbb{E}_{\tilde{\nu}}\left[e^{-(1-\gamma)\tilde{Z}}-1\right] + \frac{\rho}{1-1/\psi}(e^{(1/\psi-1)(a_I+b_Ix)}-1).
\label{eq:hjbode_affine}
\end{multline}$$ Now take the first-order Taylor approximation $$\rho e^{(1/\psi-1)(a_I+b_Ix)} \approx k_1 + k_0\left(\log{\rho}+\left(\frac{1}{\psi}-1\right)(a_I+b_Ix)\right)$$ for $k_0$ and $k_1$ defined in the proposition. Substituting this back into the HJB equation and collecting the constants and the coefficients in $x$, we get two equations, ([\[eq:valuecoeff_a_affine\]](#eq:valuecoeff_a_affine)) and a quadratic in $b_I$: $$\begin{equation*}
0 =  \frac{1}{2}\left(1-\gamma\right)\bar{\sigma}_X^{(1)}b_I^2 + (\bar{\mu}_X^{(1)} - k_0)b_I - \frac{1}{2}\gamma\bar{\tilde{\sigma}}^{(1)} + \bar{\eta}^{(1)}\frac{1}{1-\gamma}\mathbb{E}_{\tilde{\nu}}\left[e^{-(1-\gamma)\tilde{Z}}-1-(1-\gamma)(e^{-\tilde{Z}}-1)\right].
\end{equation*}$$ We thus have the explicit solution given in the proposition: $$\begin{equation*}
b_I = \frac{k_0-\bar{\mu}_X^{(1)}}{\left(1-\gamma\right)\bar{\sigma}_X^{(1)}} \pm\sqrt{\left(\frac{k_0-\bar{\mu}_X^{(1)}}{\left(1-\gamma\right)\bar{\sigma}_X^{(1)}}\right)^2+2\frac{\gamma(1-\gamma)\bar{\tilde{\sigma}}^{(1)}-\bar{\eta}^{(1)}\mathbb{E}_{\tilde{\nu}}\left[e^{-\tilde{Z}}(e^{\gamma\tilde{Z}}-1) + \gamma(e^{-\tilde{Z}}-1)\right]}{\left(1-\gamma\right)^2\bar{\sigma}_X^{(1)}}}.
\end{equation*}$$ While mathematically there are two solutions to $b_I$, only the negative root makes economic sense. One of several arguments for this is given by : in the event that $\bar{\tilde{\sigma}}^{(1)}=\bar{\eta}^{(1)}\tilde{Z}=0$, cross-sectional risk should be irrelevant to the value function ($b_I=0$), and this only occurs for the negative root.

When $\psi=1$, we can replace $\rho(e^{(1/\psi-1)(a_I+b_Ix)}-1)/(1-1/\psi)$ with $-\rho(a_I+b_Ix)$ in the ODE ([\[eq:hjbode_affine\]](#eq:hjbode_affine)). Notice, then, that the ODE in this case is identical to that in the case with a first-order Taylor approximation with $\lim_{\psi\to1}k_0=\rho$ and $\lim_{\psi\to1}(k_0\log{\rho}+k_1-\rho)/(1-1/\psi)=0$. Of course, we have not made any such approximations in this case, so our solution will be exact when $\psi=1$. ◻

From an economic perspective, the important quantity here is $b_I$. Notice that the semi-elasticity $I_X/I$, which shows up in the returns in the isoelastic economy, equals the constant $b_I$. Suppose $\gamma>1$, $\bar{\sigma}_X^{(1)}>0$, and $\bar{\mu}_X^{(1)}<0$ --- a natural assumption, if we want $X$ to be stationary. Then $b_I$ is strictly negative if and only if the second term in the square root of ([\[eq:valuecoeff_b_affine\]](#eq:valuecoeff_b_affine)) is strictly positive, suggesting that increases in cross-sectional risk have an adverse effect on agents' continuation value. If, alternatively, markets are complete, then $\bar{\tilde{\sigma}}^{(1)}=\bar{\eta}^{(1)}\tilde{Z}_t=0$ implies that $b_I=0$.

Now that we have an (approximate) explicit solution for the value function, we can substitute $I(x)$ into the asset pricing solutions from the isoelastic economy.[^44] We can begin with the riskfree rate.

**Proposition 7**. *The riskfree rate in the affine economy is given by $$\begin{multline}
r_t \approx \rho + \frac{1}{\psi}\mu_C - \frac{1}{2}\gamma\left(\frac{1}{\psi}+1\right)(|\sigma_C|^2+\bar{\tilde{\sigma}}^{(0)}+\bar{\tilde{\sigma}}^{(1)}X_t) \\
+ \frac{1}{2}b_I^2\left(\gamma-\frac{1}{\psi}\right)\left(\frac{1}{\psi}-1\right)(\bar{\sigma}_X^{(0)}+\bar{\sigma}_X^{(1)}X_t) \\
-\sum_{j=1}^n\lambda^{(j)}\mathbb{E}_{\nu_{CX}^{(j)}}\left[e^{\gamma Z_C^{(j)}+b_I(1-\gamma)Z_X^{(j)}}\left(1-\frac{1/\psi-\gamma}{1-\gamma}e^{-Z_C^{(j)}}\right) - \frac{1-1/\psi}{1-\gamma}\right] \\
- (\bar{\eta}^{(0)}+\bar{\eta}^{(1)}X_t)\mathbb{E}_{\tilde{\nu}}\left[\left(e^{\gamma\tilde{Z}}-\frac{1}{\psi}\right)\left(1-\frac{1/\psi-\gamma}{1-\gamma}e^{-\tilde{Z}}\right) - \frac{1-1/\psi}{1-\gamma}\right].
\label{eq:riskfreerate_thm_affine}
\end{multline}$$ This expression is exact when utility is time-additive or the EIS $\psi=1$.*

***Proof of Proposition 7**.* Simply substitute $I(x)$ and the coefficients into the general expression ([\[eq:riskfreeratethm1_1_theory\]](#eq:riskfreeratethm1_1_theory)). ◻

The intuition for this expression is as in the isoelastic economy; now, however, we see explicit, linear dependence on $X$. Suppose $X_t$ is positive. If idiosyncratic Brownian risk is increasing in $X$ ($\bar{\tilde{\sigma}}^{(1)}>0$), then there is a precautionary savings motive that strictly decreases the equilibrium interest rate, the magnitude of which is greater in times of high cross-sectional risk. This effect is unambiguous in that it is true for all combinations of $\gamma$ and $\psi$. Moreover, the term in the second line of ([\[eq:riskfreerate_thm_affine\]](#eq:riskfreerate_thm_affine)) represents an effect from the volatility of cross-sectional risk. It contains a joint effect of aversion to cross-sectional risk ($\gamma$ relative to $\psi$) and an intertemporal substitution effect ($\psi$ relative to unity). Provided that the volatility of cross-sectional risk is higher in times of high risk ($\bar{\sigma}_X^{(1)}>0$) and agents prefer early resolution of uncertainty, the sign of this effect comes down to the EIS: if $\psi>1$, it is negative; if $\psi<1$, it is positive; and if $\psi=1$, it is zero. Finally, there exist analogous effects related to idiosyncratic jumps, but these cannot be separated. If we shut off the latter channel by setting $\psi=1$, then we see a similar effect to that above: if the cross-sectional jump probability is increasing in $X$ ($\bar{\eta}^{(1)}>0$) and idiosyncratic jumps are always adverse events ($\tilde{Z}_t>0$ almost surely), then there is a precautionary savings effect that necessarily reduces the riskfree rate and is larger in magnitude for large $X_t$.

Using this riskfree rate expression, we can solve explicitly for the price of the stock. In the affine economy, this task becomes easier if we first individually price the *equity strips* for each maturity $\tau\geq0$. The $\tau$-maturity equity strip is the claim to only the dividend $D_{t+\tau}$; thus, the stock is the total of all the equity strips. Letting $P_t^{(\tau)}$ denote the price of the $\tau$-maturity strip, the total market is worth $S_t=\int_0^\infty P_t^{(\tau)}d\tau$.

**Lemma 5**. *The equity strip with maturity $\tau$ has price $P_t^{(\tau)}=D_tG(X_t,\tau)$, where the price-dividend ratio $$\begin{equation}
G_t^{(\tau)}\approx\exp{\{a_G(\tau)+b_G(\tau)X_t\}}
\label{eq:equitystripprice_affine}
\end{equation}$$ for functions $a_G(\tau)$ and $b_G(\tau)$ that solve the system $$\begin{multline*}
\frac{da_G(\tau)}{d\tau} = - \rho - \frac{1}{\psi}\mu_C + \frac{1}{2}\gamma\left(\frac{1}{\psi}+1\right)(|\sigma_C|^2+\bar{\tilde{\sigma}}^{(0)}) - \frac{1}{2}b_I^2\left(\gamma-\frac{1}{\psi}\right)\left(\frac{1}{\psi}-1\right)\bar{\sigma}_X^{(0)} \\
+\sum_{j=1}^n\lambda^{(j)}\mathbb{E}_{\nu_{CX}^{(j)}}\left[e^{-(1-\gamma) Z_C^{(j)}+b_I(1-\gamma)Z_X^{(j)}}\left(e^{Z_C^{(j)}-Z_D^{(j)}+b_G(\tau)Z_X^{(j)}}-\frac{1/\psi-\gamma}{1-\gamma}\right) + \frac{1-1/\psi}{1-\gamma}\right] \\
- \bar{\eta}^{(0)}\mathbb{E}_{\tilde{\nu}}\left[\left(e^{\gamma\tilde{Z}}-\frac{1}{\psi}\right)\left(\frac{1/\psi-\gamma}{1-\gamma}e^{-\tilde{Z}} - 1\right) + \frac{1-1/\psi}{1-\gamma}\right] \\
+ \bar{\mu}_D^{(0)} + b_G(\tau)\bar{\mu}_X^{(0)} +\frac{1}{2}b_G(\tau)^2\bar{\sigma}_X^{(0)} - \gamma\bar{\sigma}_{CD}^{(0)} - b_I\left(\gamma-\frac{1}{\psi}\right)\left(\bar{\sigma}_{XD}^{(0)}+b_G(\tau)\bar{\sigma}_{X}^{(0)}\right),
\end{multline*}$$ and $$\begin{multline*}
\frac{db_G(\tau)}{d\tau} = - \frac{1}{2}\gamma\left(\frac{1}{\psi}+1\right)\bar{\tilde{\sigma}}^{(1)} - \frac{1}{2}b_I^2\left(\gamma-\frac{1}{\psi}\right)\left(\frac{1}{\psi}-1\right)\bar{\sigma}_X^{(1)} \\
- \bar{\eta}^{(1)}\mathbb{E}_{\tilde{\nu}}\left[\left(e^{\gamma\tilde{Z}}-\frac{1}{\psi}\right)\left(\frac{1/\psi-\gamma}{1-\gamma}e^{-\tilde{Z}} - 1\right) + \frac{1-1/\psi}{1-\gamma}\right] \\
+\bar{\mu}_D^{(1)} + b_G(\tau)\bar{\mu}_X^{(1)}+ \frac{1}{2}b_G(\tau)^2\bar{\sigma}_X^{(1)} - \gamma\bar{\sigma}_{CD}^{(1)} - b_I\left(\gamma-\frac{1}{\psi}\right)b_G(\tau)\left(\bar{\sigma}_{XD}^{(1)}+b_G(\tau)\bar{\sigma}_{X}^{(1)}\right),
\end{multline*}$$ subject to $a_G(0)=b_G(0)=0$. Thus, the stock price takes the form $S_t=D_tF(X_t)$, where the price-dividend ratio $$F(X_t)\approx\int_0^\infty\exp{\{a_G(\tau)+b_G(\tau)X_t\}}d\tau.$$ These solutions are exact when utility is time-additive or the EIS $\psi=1$.*

***Proof of Lemma 5**.* Recall the differential equation ([\[eq:equitypde_theory\]](#eq:equitypde_theory)) characterizing $F(x)$ and its derivation in the proof of Lemma 3. Using the exact same arguments as in that proof, we can derive an analogous PDE for $G(x,\tau)$ with boundary condition $G(x,0)=1$ (the zero-maturity strip is just the claim to the current cash flow, so $P_t^{(0)}=D_t$). Now, we can substitute our conjecture for $G(x,\tau)$ into this PDE to get the relation $$\begin{multline*}
r(x) = \bar{\mu}_D^{(0)}+\bar{\mu}_D^{(1)}x + b_G(\tau)(\bar{\mu}_X^{(0)}+\bar{\mu}_X^{(1)}x) - \frac{da_G(\tau)}{d\tau} - \frac{db_G(\tau)}{d\tau}x + \frac{1}{2}b_G(\tau)^2(\bar{\sigma}_X^{(0)}+\bar{\sigma}_X^{(1)}x) \\
+ \sum_{j=1}^n\lambda^{(j)} \mathbb{E}_{\nu_{CXD}}\left[e^{\gamma Z_C^{(j)}-(\gamma-1/\psi)bZ_X^{(j)}}(e^{-Z_D^{(j)}+b_G(\tau)Z_X^{(j)}}-1)\right] \\
- \gamma(\bar{\sigma}_{CD}^{(0)}+\bar{\sigma}_{CD}^{(1)}x) - b_I\left(\gamma-\frac{1}{\psi}\right)\left(\bar{\sigma}_{XD}^{(0)}+\bar{\sigma}_{XD}^{(1)}x + b_G(\tau)\left(\bar{\sigma}_{X}^{(0)}+\bar{\sigma}_{X}^{(1)}x\right)\right)
\end{multline*}$$ Substituting in the solution ([\[eq:riskfreerate_thm_affine\]](#eq:riskfreerate_thm_affine)) for the riskfree rate and collecting constant terms and coefficients in $x$ gives us the system of equations in the lemma. Clearly, this is exact when $b_I$ (i.e., the solution for the value function) is exact, which occurs in the case of time-additive utility or unit EIS. ◻

We have thus reduced the problem to solving two first-order ordinary differential equations (ODEs). As long as these solutions are well-defined, one can simply solve the second ODE for $b_G(\tau)$ and use this solution to solve the first for $a_G(\tau)$.[^45] These solutions in hand, the risk premium and return process on the stock follow straightforwardly.

**Proposition 8**. *In the affine economy, the risk premium on the stock is given by $$\begin{equation}
r_{St}-r_t \approx \gamma\sigma_C^\top\sigma_{St} + b_I\left(\gamma-\frac{1}{\psi}\right)\sigma_{Xt}^\top\sigma_{St} + \sum_{j=1}^n\lambda^{(j)}\mathbb{E}_{\nu_{CX}^{(j)}}\left[(e^{\gamma Z_C^{(j)}-b_I(\gamma-1/\psi)Z_X^{(j)}}-1)(1-e^{-\zeta_{St}^{(j)}})\right],
\label{eq:riskpremiumthm_affine}
\end{equation}$$ where the stock diffusion coefficient $$\begin{equation*}
\sigma_{St} \approx \sigma_{D} + \left(\int_0^\infty b_G(\tau)\frac{\exp\{a_G(\tau)+b_G(\tau)X_t\}}{\int_0^\infty\exp\{a_G(\tau')+b_G(\tau')X_t\}d\tau'}d\tau\right)\sigma_{Xt}
\end{equation*}$$ and the jump coefficients $$\begin{equation*}
e^{-\zeta_{St}^{(j)}} \approx e^{-Z_{D}^{(j)}}\left(\int_0^\infty \frac{\exp\{a_G(\tau)+b_G(\tau)(X_{t^-}+Z_{Xt}^{(j)})\}}{\int_0^\infty\exp\{a_G(\tau')+b_G(\tau')X_{t^-}\}d\tau'}d\tau\right).
\end{equation*}$$ This solution is exact when utility is time-additive or the EIS $\psi=1$.*

***Proof of Proposition 8**.* Substituting the results of the affine economy into the corresponding equations from the isoelastic economy yields the results in this proposition. ◻

The interpretation of this result is like that in the isoelastic economy, but now, up to a basic integral, the expression is an explicit function of $X$. As discussed above, three assumptions matter for determining the effect of market incompleteness on risk premia. First, we know that for there to be any effect at all in this case, utility must be non-time-additive. Second, if this is the case, we can look to the the signs of the semi-elasticity $I_X/I=b_I$ and of the covariance $\sigma_{Xt}^\top\sigma_{St}$. Evidently, the irrelevance results that held in the isoelastic economy continue to hold in this special case. So as not to belabor the point, I pursue further discussion of this result in Section 3 (the human-capital model), for which these results continue to hold.

# Proofs of results in Section 3 

***Proof of Proposition 5**.* The HJB equation ([\[eq:hjb_model\]](#eq:hjb_model)) can be written out in full (suppressing $t$ subscripts) as $$\begin{multline}
0 = \sup_{\left\{C_i,x_i,\alpha_H^{(i)},\alpha_S^{(i)}\right\}} \biggl\{J_W^{(i)}\biggl(W_i\biggl[\alpha_H^{(i)}\left(\frac{a-x_i}{q_i}+\Phi(x_i)-\delta-\eta\mathbb{E}_{\tilde{\nu}}[e^{-\tilde{Z}}-1]-r\right)  \\
+ \alpha_S^{(i)}\left(F^{-1} + \mu_S - r\right)+r\biggr] - C_i\biggr) + J_\eta^{(i)}\kappa_\eta(\bar{\eta}-\eta) + J_{W\eta}^{(i)}W_i\alpha_S^{(i)}\sigma_S^{(\eta)}\sigma_\eta\sqrt{\eta}  \\
+ \frac{1}{2}J_{WW}^{(i)}W_i^2 \left(\left(\alpha_H^{(i)}\sigma+\alpha_S^{(i)}\sigma_S^{(H)}\right)^2+\alpha_S^{(i)2}\sigma_S^{(\eta)2}+\alpha_H^{(i)2}\tilde{\sigma}^2\right) + \frac{1}{2}J_{\eta\eta}^{(i)}\sigma_\eta^2\eta \\
+ \lambda\mathbb{E}_{\nu}\bigl[J^{(i)}(W_i(1+\alpha_H^{(i)}(e^{-Z}-1)+\alpha_S^{(i)}(e^{-\zeta_S}-1)),\eta) - J^{(i)}(W_i,\eta)\bigr] \\
+ \eta\mathbb{E}_{\tilde{\nu}}\left[J^{(i)}(W_i(1+\alpha_H^{(i)}(e^{-\tilde{Z}}-1)),\eta)-J^{(i)}(W_i,\eta)\right] + \bar{f}(C_i,J^{(i)}(W_i,\eta)) \biggr\}.
\label{eq:hjb_model_app}
\end{multline}$$ The first-order conditions of the capital share $\alpha_{Ht}^{(i)}$ is $$\begin{multline}
0 = J_W^{(i)}W_{it}\left(\frac{a-x_{it}}{q_i}+\Phi(x_{it})-\delta-\eta_t\mathbb{E}_{\tilde{\nu}}[e^{-\tilde{Z}}-1]-r_t\right) + J_{WW}^{(i)}W_{it}^2\left(\alpha_{Ht}^{(i)}(\sigma^2+\tilde{\sigma}^2) +\alpha_{St}^{(i)}\sigma\sigma_{St}\right)\\
+ \lambda\mathbb{E}_{\nu}\bigl[J_{\alpha_H}^{(i)}(W_{it}(1+\alpha_{Ht}^{(i)}(e^{-Z}-1)+\alpha_{St}^{(i)}(e^{-\zeta_{St}}-1)),\eta_t)\bigr] \\
+ \eta_t\mathbb{E}_{\tilde{\nu}}\bigl[J_{\alpha_H}^{(i)}(W_{it}(1+\alpha_{Ht}^{(i)}(e^{-\tilde{Z}}-1)),\eta_t)\bigr],
\label{eq:focalphah_model}
\end{multline}$$ and that of the equity share $\alpha_{St}^{(i)}$ is $$\begin{multline}
0 = J_W^{(i)}W_{it}(F_t^{-1}+\mu_{St}-r_t) + J_{WW}^{(i)}W_{it}^2\left(\alpha_{St}^{(i)}(\sigma^{(H)2}_{St}+\sigma^{(\eta)2}_{St}) +\alpha_{Ht}^{(i)}\sigma\sigma_{St}\right) \\
+ J_{W\eta}^{(i)}W_{it}\sigma_{St}^{(\eta)}\sigma_\eta\sqrt{\eta_t} + \lambda\mathbb{E}_{\nu}\bigl[J_{\alpha_S}^{(i)}(W_{it}(1+\alpha_{Ht}^{(i)}(e^{-Z}-1)+\alpha_{St}^{(i)}(e^{-\zeta_{St}}-1)),\eta_t)\bigr].
\label{eq:focalphas_model}
\end{multline}$$ Conjecture that the value function is indeed of the form ([\[eq:valuefuncsol1_affine\]](#eq:valuefuncsol1_affine))--([\[eq:valuefuncsol2_affine\]](#eq:valuefuncsol2_affine)). The first-order condition for the capital share ([\[eq:focalphah_model\]](#eq:focalphah_model)) becomes $$\begin{multline*}
0 = \frac{a-x_{it}}{q_i}+\Phi(x_{it})-\delta-\eta_t\mathbb{E}_{\tilde{\nu}}[e^{-\tilde{Z}}-1]-r_t - \gamma\left(\alpha_{Ht}^{(i)}(\sigma^2+\tilde{\sigma}^2) +\alpha_{St}^{(i)}\sigma\sigma_{St}\right) \\
+ \lambda\mathbb{E}_{\nu}\bigl[(1+\alpha_{Ht}^{(i)}(e^{-Z}-1)+\alpha_{St}^{(i)}(e^{-\zeta_{St}}-1))^{-\gamma}(e^{-Z}-1)\bigr] \\
+ \eta_t\mathbb{E}_{\tilde{\nu}}\bigl[(1+\alpha_{Ht}^{(i)}(e^{-\tilde{Z}}-1))^{-\gamma}(e^{-Z}-1)\bigr].
\end{multline*}$$ Likewise, the first-order condition for the equity share ([\[eq:focalphas_model\]](#eq:focalphas_model)) becomes $$\begin{multline*}
0 = F_t^{-1}+\mu_{St}-r_t -\gamma\left(\alpha_{St}^{(i)}(\sigma^{(H)2}_{St}+\sigma^{(\eta)2}_{St}) +\alpha_{Ht}^{(i)}\sigma\sigma_{St}\right) + (1-\gamma)b_I\sigma_{St}^{(\eta)}\sigma_\eta\sqrt{\eta_t} \\
+ \lambda\mathbb{E}_{\nu}\bigl[(1+\alpha_{Ht}^{(i)}(e^{-Z}-1)+\alpha_{St}^{(i)}(e^{-\zeta_{St}}-1))^{-\gamma}(e^{-\zeta_{St}}-1)\bigr].
\end{multline*}$$ Notice that these two conditions are identical for all agents, so it must be the case that $\alpha_{Ht}^{(i)}=\alpha_{Ht}^{(i')}$ and $\alpha_{St}^{(i)}=\alpha_{St}^{(i')}$ for all $(i,i')\in\mathcal{I}\times\mathcal{I}$. The fact that the stock is in zero net supply then implies that $\alpha_S=0$. Similarly, the fact that the bond is in zero net supply means that $$0 = \int_\mathcal{I}W_{it}(1-\alpha_{Ht}^{(i)}-\alpha_{St}^{(i)})di = \int_\mathcal{I}W_{it}di(1-\alpha_{Ht}),$$ which can only hold for $\alpha_H=1$. Now, substituting the value function into the envelope condition ([\[eq:foccons_model\]](#eq:foccons_model)) implies that $$C_{it} = \rho W_{it}.$$ Since $\alpha_H=1$ and $\alpha_S=0$, every agent holds a zero position in the bond and stock, and wealth simply equals the value of an individual's human capital: $W_{it}=q_iH_{it}$. Finally, note that this value of wealth, clearing of the goods market ($C_{it}=(a-x_{it})H_{it}$), and the optimal consumption policy combine to imply that $$a-x_{it} = \rho q_i.$$ From this equation and the first-order condition for capital investment ([\[eq:focx_model\]](#eq:focx_model)), we get the solution for $x$ and $q$ stated in the proposition.

All that remains is to verify the conjecture for the value function. Substitute the conjecture and the optimal controls into the HJB equation ([\[eq:hjb_model\]](#eq:hjb_model)), and divide by $W_{it}^{1-\gamma}I(\eta_t)^{1-\gamma}$: $$\begin{multline*}
0 = \Phi(x)-\delta-\eta_t\mathbb{E}_{\tilde{\nu}}[e^{-\tilde{Z}}-1] + b_I\kappa_\eta(\bar{\eta}-\eta_t) - \frac{1}{2}\gamma(\sigma^2+\tilde{\sigma}^2) + \frac{1}{2}(1-\gamma)b_I^2\sigma_\eta^2\eta_t \\
+ \frac{1}{1-\gamma}\lambda\mathbb{E}_{\nu}[e^{-(1-\gamma)Z}-1] + \frac{1}{1-\gamma}\eta_t\mathbb{E}_{\tilde{\nu}}[e^{-(1-\gamma)\tilde{Z}}-1] + \rho(\log\rho-a_I-b_I\eta_t).
\end{multline*}$$ Collecting constants gives us ([\[eq:valuecoeff_a_model\]](#eq:valuecoeff_a_model)); collecting coefficients in $\eta_t$ gives us a quadratic function of $b_I$, $$\begin{equation*}
0 =\frac{1}{2}(1-\gamma)\sigma_\eta^2b_I^2 - (\rho + \kappa_\eta)b_I + \frac{1}{1-\gamma} \mathbb{E}_{\tilde{\nu}}[e^{-(1-\gamma)\tilde{Z}}-1] - \mathbb{E}_{\tilde{\nu}}[e^{-\tilde{Z}}-1],
\end{equation*}$$ the solution to which is ([\[eq:valuecoeff_b_model\]](#eq:valuecoeff_b_model)). For an explanation of why we take the negative root only, see the proof of Proposition 6. ◻

***Proof of Lemma 4**.* Simplifying the differential equations in Lemma 5 gives us $$\begin{multline*}
\frac{da_G(\tau)}{d\tau} = - \rho - \Phi(x) + \delta + \gamma((1-\phi)\sigma^2+\tilde{\sigma}^2) +\lambda\mathbb{E}_{\nu}\left[e^{-(1-\gamma) Z}(e^{(1-\phi)Z}-1)\right] \\
+ \phi(\Phi(x)-\delta)+\frac{1}{2}\phi(\phi-1)\sigma^2 + \kappa_\eta\bar{\eta}b_G(\tau),
\end{multline*}$$ and $$\begin{equation*}
\frac{db_G(\tau)}{d\tau} = - \mathbb{E}_{\tilde{\nu}}\left[(e^{\gamma\tilde{Z}}-1)(e^{-\tilde{Z}} - 1)\right] + (b_I\left(1-\gamma\right)\sigma_\eta^2 - \kappa_\eta)b_G(\tau) + \frac{1}{2}\sigma_\eta^2b_G(\tau)^2.
\end{equation*}$$ Substituting in the equations stated in the proposition verifies the solution; these expressions also satisfy the boundary conditions $a_G(0)=b_G(0)=0$. ◻

# Details of a more general theory 

As discussed in Section 2.7, the main theoretical results of the paper generalize to an even more general economic setting. This appendix section lays out and proves these results. Certain proofs and details are relegated to the end, in Section 10.5.

## Economic setting

Consider the economic setting described in Section 2.1. Let us generalize Assumption 5, which defines preferences, to allow for cross-agent heterogeneity and non-standard functional forms.

**Assumption 8** (Preferences). *Each agent $i\in\mathcal{I}$ has a $C^{3,1}$ felicity function $\bar{f}^{(i)}:\mathcal{C}\times\mathbb{R}\to\mathbb{R}$, denoted $\bar{f}^{(i)}(c,v)$, satisfying the following conditions:*

1.  *Adaptability: For each fixed $\{c,v\}\in\mathcal{C}\times\mathbb{R}$, $\bar{f}^{(i)}(c,v)$ is an adapted process.*

2.  *Uniform Lipschitz condition: for each $\{c,v,v'\}\in\mathcal{C}\times\mathbb{R}\times\mathbb{R}$, there exists a constant $K\in\mathbb{R}$ such that $|\bar{f}^{(i)}(c,v)-\bar{f}^{(i)}(c,v')|\leq K|v-v'|$.*

3.  *Uniform growth condition: for each $c\in\mathcal{C}$, there exists a constant $K\in\mathbb{R}$ such that $|\bar{f}^{(i)}(c,0)|\leq K(1+|c|)$.*

As show, if these three assumptions hold, then there exists a unique value function process $V_i$ satisfying the same recursion as under isoelastic utility.

Since asset-pricing moments will depend on marginal felicity functions, an assumption on these derivatives is necessary. Before making this assumption, note that, in certain equilibria, consumption processes and asset returns depend on the consumption shares of a subset of agents. Let $\hat{\mathcal{I}}\subseteq\mathcal{I}$ represent this subset, and let $\hat{\Theta}_t=\{\theta_{\hat{\imath}t}:\hat{\imath}\in\hat{\mathcal{I}}\}\subseteq\Theta_t$ denote the set of their consumption shares.[^46] Marginal felicity is then potentially a function of $C$, $\hat{\Theta}$, and $X$.

**Assumption 9** (Marginal felicity). *For all agents $i\in\mathcal{I}$, the marginal felicity function $f_C^{(i)}:\mathcal{C}\times\hat{\Theta}\times\mathbb{R}\to\mathbb{R}$ is strictly positive on its domain, and satisfies the conditions $$\lim_{c\downarrow0}f_C^{(i)}(c,\hat{\theta},x)=+\infty\quad\textrm{and}\quad\lim_{c\uparrow+\infty}f_C^{(i)}(c,\hat{\theta},x)=0.$$ Moreover, the derivative of marginal felicity with respect to consumption $f_{CC}^{(i)}(c,\hat{\theta},x)$ is strictly negative on its domain. $f_{CCC}^{(i)}(c,\hat{\theta},x)$ is strictly positive on its domain.*

These assumptions are weak and customary. We impose them so that felicity is strictly increasing and concave in consumption and so that agents optimally choose a positive level of consumption, consistent with the stochastic process assumed by ([\[eq:idioconsumpprocess_setting\]](#eq:idioconsumpprocess_setting)). Note that Assumptions 8 and 9 nest identical isoelastic utility (Assumption 5) as a special case.

## Equilibrium conditions 

The equilibrium results in Lemmas 1 and 3 continue to hold in this more general economy, with minor changes.[^47] The first difference is that marginal felicity may now depend on consumption shares $\hat{\Theta}$, in which case so too will the state-price densities ([\[eq:statepricedensity_theory\]](#eq:statepricedensity_theory)). The second difference is that the stock price may now also be a function of both aggregate consumption and individual consumption shares: $$S_t = D_tF(C_t,\hat{\Theta}_t,X_t).$$ Hence, the equity-risk coefficients ([\[eq:equitydiffusion_theory\]](#eq:equitydiffusion_theory)) and ([\[eq:equityjump_theory\]](#eq:equityjump_theory)) become, respectively, $$\begin{equation}
\sigma_{St} = \sigma_D + \frac{F_{Ct}}{F_t}\sigma_C + \int_{\hat{\mathcal{I}}}\frac{F_{\theta_{\hat{\imath}}t}}{F_t}\theta_{\hat{\imath}t}\sigma_{\theta t}^{(\hat{\imath})}d\hat{\imath} + \frac{F_{Xt}}{F_t}\sigma_{Xt}
\label{eq:equityvolatility_gentheory}
\end{equation}$$ and $$\begin{equation}
e^{-\zeta_{St}^{(j)}} = e^{-\zeta_D^{(j)}}\frac{F(C_{t^-}e^{-\zeta_C},\bigl\{\theta_{\hat{\imath}t^-}e^{\zeta_{\theta t}^{(\hat{\imath})}}\bigr\}_{\hat{\imath}\in\hat{\mathcal{I}}},X_{t^-}+\zeta_{Xt}^{(j)})}{F(C_{t^-},\hat{\Theta}_{t^-},X_{t^-})}.
\label{eq:equityjump_gentheory}
\end{equation}$$

## Asset pricing solutions 

### Aggregate variables

Because agents' preferences and equilibrium consumption levels may be heterogeneous, it will be most intuitive to express asset returns in terms of aggregates. This will also make straightforward the comparison of the complete-market benchmark with the full incomplete-market economic setting. As we will see, the variables defined in this section have as special cases the values that arise in the representative-agent benchmark.

Let us first define *aggregate risk aversion* as $$\begin{equation}
\gamma_{Ct}^{(A)} = \left(\int_\mathcal{I}\frac{C_{it}}{C_t}\left(-\frac{C_{it}f^{(i)}_{CC}(C_{it},\hat{\Theta}_t,X_t)}{f^{(i)}_C(C_{it},\hat{\Theta}_t,X_t)}\right)^{-1}di\right)^{-1}.
\label{eq:riskaversion_agg_theory}
\end{equation}$$ This is the consumption-weighted harmonic average of the local curvature of agents' felicity functions $\gamma_{C}^{(i)}=-cf_{CC}^{(i)}/f_C^{(i)}$.[^48] Likewise, we can define the *aggregate systematic precautionary savings motive* as $$\begin{equation}
\xi_{Ct}^{(A)} = \int_\mathcal{I}\frac{C_{it}}{C_t}\left(-\frac{C_{it}f_{CCC}^{(i)}(C_{it},\hat{\Theta}_t,X_t)}{f_{CC}^{(i)}(C_{it},\hat{\Theta}_t,X_t)}\right)|\sigma_{Ct}^{(i)}|^2di.
\label{eq:precautionarysavings_agg_theory}
\end{equation}$$ This variable is the consumption-weighted average of individual precautionary savings from systematic Brownian risk. The expression $-cf_{CCC}^{(i)}/f_{CC}^{(i)}$ is agent $i$'s relative prudence (Kimball 1990). In the same way, define the *aggregate idiosyncratic precautionary savings motive* $$\begin{equation}
\tilde{\xi}_{t}^{(A)} = \int_\mathcal{I}\frac{C_{it}}{C_t}\left(-\frac{C_{it}f_{CCC}^{(i)}(C_{it},\hat{\Theta}_t,X_t)}{f_{CC}^{(i)}(C_{it},\hat{\Theta}_t,X_t)}\right)\tilde{\sigma}_t^2di.
\label{eq:precautionarysavings_idio_theory}
\end{equation}$$ The objects ([\[eq:riskaversion_agg_theory\]](#eq:riskaversion_agg_theory)) through ([\[eq:precautionarysavings_idio_theory\]](#eq:precautionarysavings_idio_theory)) are standard concepts in asset pricing, reducing in the case of identical power utility to $\gamma$, $\gamma(\gamma+1)|\sigma_{C}^{(A)}|^2$, and $\gamma(\gamma+1)\tilde{\sigma}_t^2$, respectively.

Furthermore, we can use the *consumption-risk-tolerance (CRT) weights* $$\begin{equation*}
\omega_t^{(i)} = \frac{\frac{C_{it}}{C_t}\gamma_{Ct}^{(i)-1}}{\int_\mathcal{I}\frac{C_{i't}}{C_t}\gamma_{Ct}^{(i')-1}di'}
\label{eq:consrisktoleranceweights_agg_theory}
\end{equation*}$$ to define several variables that will be relevant in characterizing asset prices.[^49] Evidently, agents will have larger CRT weights if they have both a higher consumption share and lower risk aversion $\gamma_{Ct}^{(i)}$. First, define the CRT-weighted average $$\begin{equation}
f_{Vt}^{(A)} = \int_\mathcal{I}\omega_t^{(i)}f_V^{(i)}(C_{it},\hat{\Theta}_t,X_t)di.
\label{eq:partialvalue_agg_theory}
\end{equation}$$ as the *aggregate marginal felicity of value*.[^50] Similarly, for each $j\in\{1,\dots,n\}$, denote by $$\begin{equation}
\mathcal{J}_{C\hat{\Theta}X,t}^{(A,j)} = \int_\mathcal{I}\omega_t^{(i)}\frac{f_{C}^{(i)}(C_{it^-}e^{-\zeta_{Ct}^{(i,j)}},\bigl\{\theta_{\hat{\imath}t^-}e^{\zeta_{\theta t}^{(\hat{\imath})}}\bigr\}_{\hat{\imath}\in\hat{\mathcal{I}}},X_{t^-}+\zeta_{Xt}^{(j)})}{f_{C}^{(i)}(C_{it^-},\hat{\Theta}_{t^-},X_{t^-})}di
\label{eq:jumpgamma_agg_theory}
\end{equation}$$ the *aggregate systematic marginal felicity jump* corresponding to Poisson jump $j$. Evidently, this variable represents the CRT-weighted average of the gross percent change in marginal felicity, given the realization of a jump. In the event that marginal felicity is not a function of shares $\hat{\Theta}$ or cross-sectional risk $X$ for any agent --- that is, when $f_C^{(i)}(c,\hat{\theta},x)=f_C^{(i)}(c)$ --- I instead use the notation $\mathcal{J}_{Ct}^{(A,j)}$. Analogously, let $$\begin{equation}
\tilde{\mathcal{J}}_{Ct}^{(A)} = \int_\mathcal{I}\omega_t^{(i)}\frac{f_{C}^{(i)}(C_{it^-}e^{-\tilde{\zeta}_t},\bigl\{\theta_{\hat{\imath}t^-}e^{-\tilde{\zeta}_t}\bigr\}_{\hat{\imath}\in\hat{\mathcal{I}}},X_{t^-})}{f_{C}^{(i)}(C_{it^-},\hat{\Theta}_{t^-},X_{t^-})}di
\label{eq:jumpgamma_idio_theory}
\end{equation}$$ represent the *aggregate idiosyncratic marginal felicity jump*. In the standard power utility case, we then get $\mathcal{J}_{Ct}^{(A,j)}=e^{\gamma\zeta_C^{(j)}}$ and $\tilde{\mathcal{J}}_{Ct}^{(A)}=e^{\gamma\tilde{\zeta}_t}$.

Finally, foreseeing that marginal felicity will, under certain assumptions, depend on the states $\hat{\Theta}$ and $X$, we can define some aggregate variables related to these state variables. Let $$\begin{equation}
\gamma_{Xt}^{(A)} = \int_\mathcal{I}\omega_t^{(i)}\left(-\frac{f_{CX,t}^{(i)}}{f_{Ct}^{(i)}}\right)di.
\end{equation}$$ denote *aggregate aversion to cross-sectional risk*. The value $f_{CX}^{(i)}/f_C^{(i)}$ is the semi-elasticity of marginal felicity with respect to cross-sectional risk.[^51] If, as one might expect, an increase in cross-sectional risk increases marginal felicity (i.e., if it is an undesirable outcome), then $f_{CX}^{(i)}/f_C^{(i)}$ is positive and this aggregate variable is negative. Define $\gamma_{\theta_{\hat{\imath}}}^{(A)}$ analogously.

### Equilibrium returns

Generalizing our main irrelevance results requires solving for riskfree rates and risk premia in the complete- and incomplete-market economies. The intuition behind these expressions is mostly the same, except that (i) they must be aggregated across agents and (ii) they contain effects from the changing distribution of consumption shares. I begin with the complete market.

**Proposition 9**. *In the complete-market economy, the equilibrium riskfree rate is given by[^52] $$\begin{equation}
r_t^{\rm CM} = -f_{Vt}^{(A)} + \gamma_{Ct}^{(A)}\mu_C - \frac{1}{2}\gamma_{Ct}^{(A)}\xi_{Ct}^{(A)} - \sum_{j=1}^n\lambda^{(j)}\mathbb{E}_{\nu_{C}^{(j)}}\left[\mathcal{J}_{C\hat{\Theta},t}^{(A,j)}-1\right] + \Xi_{\hat{\Theta}t} 
\label{eq:riskfreerate_cm_theory}
\end{equation}$$ where $\Xi_{\hat{\Theta}t}$, given by ([\[eq:xishare_systematic\]](#eq:xishare_systematic)), captures the effect of systematic shocks to consumption shares.*

Similarly, we can solve for the price of the stock and its expected excess return.

**Proposition 10**. *In the complete-market economy, the risk premium on the stock is given by $$\begin{equation}
r_{St}^{\rm CM}-r_t^{\rm CM} =  \gamma_{Ct}^{(A)}\sigma_C^\top\sigma_{St} + \int_{\hat{\mathcal{I}}}\gamma_{\theta_{\hat{\imath}}t}^{(A)}\theta_{\hat{\imath}t}\sigma_{\theta t}^{(\hat{\imath})\top}\sigma_{St}d\hat{\imath} + \sum_{j=1}^n\lambda^{(j)}\mathbb{E}_{\nu_{CD}^{(j)}}\left[\left(\mathcal{J}_{C\hat{\Theta}t}^{(A,j)}-1\right)(1-e^{-\zeta_{St}^{(j)}})\right],
\end{equation}$$ where the equity-risk coefficients $$\begin{equation*}
\sigma_{St} = \sigma_D + \frac{F_{Ct}}{F_t}\sigma_C  + \int_{\hat{\mathcal{I}}}\frac{F_{\theta_{\hat{\imath}}t}}{F_t}\theta_{\hat{\imath}t}\sigma_{\theta t}^{(\hat{\imath})}d\hat{\imath} \quad\textrm{and}\quad e^{-\zeta_{St}^{(j)}} = e^{-\zeta_D^{(j)}}\frac{F(C_{t^-}e^{-\zeta_C},\bigl\{\theta_{\hat{\imath}t^-}e^{\zeta_{\theta t}^{(\hat{\imath})}}\bigr\}_{\hat{\imath}\in\hat{\mathcal{I}}})}{F(C_{t^-},\hat{\Theta}_{t^-})}.
\end{equation*}$$*

Likewise, we can solve for the corresponding incomplete-market interest rate.

**Proposition 11**. *In the incomplete-market economy, the equilibrium riskfree rate is given by $$\begin{multline}
r_t =  -f_{Vt}^{(A)} + \gamma_{Ct}^{(A)}\mu_C - \frac{1}{2}\gamma_{Ct}^{(A)}\xi_{Ct}^{(A)} -\sum_{j=1}^n\lambda^{(j)}\mathbb{E}_{\nu_{CX}^{(j)}}\left[\mathcal{J}_{C\hat{\Theta}X,t}^{(A,j)} - 1\right] + \Xi_{\hat{\Theta}t} \\
- \frac{1}{2}\gamma_{Ct}^{(A)}\tilde{\xi}_t^{(A)} - \eta_t \mathbb{E}_{\tilde{\nu}}\left[\tilde{\mathcal{J}}_{Ct}^{(A)}-1+\gamma_{Ct}^{(A)}(e^{-\tilde{\zeta}_t}-1)\right] + \tilde{\Xi}_{\hat{\Theta}t} + \Xi_{Xt},
\label{eq:riskfreeratethm1_1_gentheory}
\end{multline}$$ where $\Xi_{\hat{\Theta}t}$ is as in the complete-market economy; $\tilde{\Xi}_{\hat{\Theta}t}$, given by ([\[eq:xishare_idio\]](#eq:xishare_idio)), captures the effect of idiosyncratic shocks to consumption shares; and $\Xi_{Xt}$, given by ([\[eq:xicrosssec\]](#eq:xicrosssec)), captures the effect of time-variation in cross-sectional risk.*

And, lastly, we can solve for the incomplete-market risk premium.

**Proposition 12**. *In the incomplete-market economy, the risk premium on the stock is given by $$\begin{multline}
r_{St}-r_t =  \gamma_{Ct}^{(A)}\sigma_C^\top\sigma_{St} + \int_{\hat{\mathcal{I}}}\gamma_{\theta_{\hat{\imath}}t}^{(A)}\theta_{\hat{\imath}t}\sigma_{\theta t}^{(\hat{\imath})\top}\sigma_{St}d\hat{\imath} + \gamma_{Xt}^{(A)}\sigma_{Xt}^\top\sigma_{St}\\
+ \sum_{j=1}^n\lambda^{(j)}\mathbb{E}_{\nu_{CXD}^{(j)}}\left[\left(\mathcal{J}_{C\hat{\Theta}X,t}^{(A,j)}-1\right)(1-e^{-\zeta_{St}^{(j)}})\right],
\label{eq:riskpremiumthm1_gentheory}
\end{multline}$$ where the equity-risk coefficients are given by ([\[eq:equityvolatility_gentheory\]](#eq:equityvolatility_gentheory)) and ([\[eq:equityjump_gentheory\]](#eq:equityjump_gentheory)).*

## When does idiosyncratic risk matter? 

Recall the formal definitions of "stochastic\" and "time-varying\" cross-sectional risk in Section 2.4. As under isoelastic preferences, the effect of cross-sectional risk on returns will depend critically on the form of agents' felicity functions. The following definition establishes a particularly important property in this regard.

**Definition 5**. *We say that felicity $\bar{f}^{(i)}$ is *additively separable* if $\bar{f}^{(i)}(c,v)=u^{(i)}(c)+g^{(i)}(v)$ for some functions $u^{(i)}$ and $g^{(i)}$ that are consistent with Assumptions 8 and 9. We say that it is *time-additive* if it is additively separable with $g^{(i)}(v)=-\rho^{(i)}v$ for some constant $\rho^{(i)}$.*

The distinction between additive separability and time-additivity is mostly a mathematical formality. In practice --- namely, under isoelastic recursive preferences --- these are usually equivalent properties. Regardless, it is the economic intuition for additive separability that matters: if felicity is additively separable, then marginal felicity of today's consumption is independent of the continuation value. The following lemma affirms an exact relationship between the dynamics of cross-sectional risk and the form of the felicity function.

**Lemma 6**. *Marginal felicity $f_C^{(i)}$ is a function of cross-sectional risk $X$ if and only if $\bar{f}^{(i)}$ is non-additively-separable and $X$ is time-varying.*

This lemma will be useful for understanding whether, when, and how cross-sectional risk and agents' preferences affect prices. An analogous statement holds for the consumption shares $\hat{\Theta}_t$ by identical logic. This lemma tells us when incomplete markets can affect the price of risk; the next lemma concerns the aggregate consumption risks faced by each individual agent in equilibrium, given idiosyncratic risks and separability.[^53]

**Lemma 7**. *Consider an arbitrary time-$t$ consumption distribution $\{C_{it}:i\in\mathcal{I}\}$ that is the same in the complete- and incomplete-market economies. If all agents $i\in\mathcal{I}$ have additively separable preferences, then the exposure of all agents' consumption growth to aggregate shocks is the same in the complete- and incomplete-market economies: $\forall i\in\mathcal{I}$, $\sigma_{Ct}^{(i)}=\sigma_{Ct}^{{\rm CM}(i)}=(\gamma_{Ct}^{(A)}/\gamma_{Ct}^{(i)})\sigma_C$, and each $\zeta_{Ct}^{(i,j)}=\zeta_{Ct}^{{\rm CM}(i,j)}$ solves $$C_te^{-\zeta_C^{(j)}} = \int_\mathcal{I}u_C^{(i')-1}\left(u_C^{(i')}(C_{i't})\frac{u_C^{(i)}(C_{it}e^{-\zeta_{Ct}^{(i,j)}})}{u_C^{(i)}(C_{it})}\right)di'.$$ Given additive separability, we also have that $\sigma_{Ct}^{(i)}=\sigma_C$ and $\zeta_{Ct}^{(i,j)}=\zeta_C^{(j)}$ if and only if all agents have identical, time-additive power or log utility.*

Lemmas 6 and 7 combine to give us a special case of the incomplete-market riskfree rate, which is both informative and useful for proving subsequent results.

**Lemma 8**. *Consider an arbitrary time-$t$ consumption distribution $\{C_{it}:i\in\mathcal{I}\}$ that is the same in the complete- and incomplete-market economies. If all agents $i\in\mathcal{I}$ have additively separable preferences, then the riskfree rate in the incomplete-market economy $$\begin{equation}
r_t =  r_t^{\rm CM} + \underbrace{(f_{Vt}^{{\rm CM}(A)}-f_{Vt}^{(A)})}_{=g_{Vt}^{{\rm CM}(A)}-g_{Vt}^{(A)}} - \frac{1}{2}\gamma_{Ct}^{(A)}\tilde{\xi}_t^{(A)} - \eta_t\mathbb{E}_{\tilde{\nu}}\left[\tilde{\mathcal{J}}_{Ct}^{(A)}-1+\gamma_{Ct}^{(A)}(e^{-\tilde{\zeta}_t}-1)\right].
\label{eq:riskfreeratethm1_2_gentheory}
\end{equation}$$*

The key takeaway from this theorem is that the riskfree rate is *always* affected by the precautionary savings motive from idiosyncratic risk. Even without any kind of dependence of marginal felicity on the state variables $X$ and $\hat{\Theta}$, and even if cross-sectional risk $X$ is non-time-varying, the riskfree rate differs from that of the complete-market economy by an additional quantity that is driven by agents' precautionary savings motive from idiosyncratic risk.

With these lemmas in hand, we can generalize Theorem 2 from the main paper.[^54] For simplicity, and without loss of generality, I make two changes. First, I state this theorem in terms of irrelevance instead of relevance. Second, I take stochastic cross-sectional risk as a given, since its role is obvious.

**Theorem 3**. *Suppose that cross-sectional risk $X$ is stochastic. Market incompleteness is irrelevant for risk premia if and only if both of the following conditions hold:*

1.  *All agents $i\in\mathcal{I}$ have identical, time-additive power or log utility.*

2.  *Aggregate consumption shocks are uncorrelated with shocks to cross-sectional risk (i.e., $\sigma_C^\top\sigma_{Xt}=\zeta_C^{(j)}\zeta_{Xt}^{(j)}=0$ almost surely).*

Of course, the contrapositive is also true. The second condition is identical to that in the main text. The intuition for the first condition is as follows. In the first place, irrelevance requires additively separable preferences, so that marginal felicity is independent of continuation value. In the second place, it requires identical power utility because its isoelasticity and homotheticity means consumption shares $\hat{\Theta}$ are no longer a state variable. As the proof of this theorem shows, consumption shares being a state variable implies a change in the equity risks (through $\sigma_S$ and $\zeta_S^{(j)}$) for which agents demand compensation. In other words, the only way in which compensation for stochastic consumption shares can be irrelevant is if individual exposure to systematic consumption risk is identical across agents, and we know from Lemma [\[lemma:consumpcoeffs_theory\]](#lemma:consumpcoeffs_theory) that this only occurs given identical power or log utility.

## Proofs for a more general theory 

***Proof of Proposition 9 and 10**.* The logic is the same as in the proof of Propositions 1 and 2. Applying this logic to the incomplete-market solutions in Propositions 11 and 12 yields the stated solutions. ◻

***Proof of Proposition 11**.* Applying Itô's lemma to the state-price density for agent $i$ and substituting into the riskfree rate equation ([\[eq:riskfreerate_general_theory\]](#eq:riskfreerate_general_theory)), we get $$\begin{multline*}
r_t = -f_{Vt}^{(i)}-\frac{f_{CC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}\mu_{Ct}^{(i)} -\frac{1}{2}\frac{f_{CCC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}^2(|\sigma_{Ct}^{(i)}|^2 + \tilde{\sigma}_t^2) \\
-\sum_{j=1}^n\lambda^{(j)}\mathbb{E}_{\nu_{CX}^{(j)}}\left[\frac{f_{C}^{(i)}(C_{it^-}e^{-\zeta_{Ct}^{(i,j)}},\bigl\{\theta_{\hat{\imath}t^-}e^{\zeta_{\theta t}^{(\hat{\imath})}}\bigr\}_{\hat{\imath}\in\hat{\mathcal{I}}},X_{t^-}+\zeta_{Xt}^{(j)})}{f_{C}^{(i)}(C_{it^-},\hat{\Theta}_{t^-},X_{t^-})}-1\right]\\
 - \eta_t\mathbb{E}_{\tilde{\nu}}\left[\frac{f_{C}^{(i)}(C_{it^-}e^{-\tilde{\zeta}_t},\hat{\Theta}_{t^-},X_{t^-})}{f_{C}^{(i)}(C_{it^-},\hat{\Theta}_{t^-},X_{t^-})}-1-\frac{f_{CC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}(e^{-\tilde{\zeta}_t}-1)\right]\\
-  \int_{\hat{\mathcal{I}}}\frac{f_{C\theta_{\hat{\imath}},t}^{(i)}}{f_{Ct}^{(i)}}\theta_{\hat{\imath}t}\mathbb{E}_{\tilde{\nu}}[\bar{\mu}_{\theta t}^{(\hat{\imath})}]d\hat{\imath} -\frac{1}{2}\int_{\hat{\mathcal{I}}}\int_{\hat{\mathcal{I}}}\frac{f_{C\theta_{\hat{\imath}}\theta_{\hat{\imath}'},t}^{(i)}}{f_{Ct}^{(i)}}\theta_{\hat{\imath}t}\theta_{\hat{\imath}'t}\sigma_{\theta t}^{(\hat{\imath})\top}\sigma_{\theta t}^{(\hat{\imath}')}d\hat{\imath}d\hat{\imath}' - \int_{\hat{\mathcal{I}}}\frac{f_{CC\theta_{\hat{\imath}},t}^{(i)}}{f_{Ct}^{(i)}}C_{it}\theta_{\hat{\imath}t}\sigma_{Ct}^{(i)\top}\sigma_{\theta t}^{(\hat{\imath})}d\hat{\imath} \\
 - \frac{1}{2}\int_{\hat{\mathcal{I}}}\frac{f_{C\theta_{\hat{\imath}}\theta_{\hat{\imath}},t}^{(i)}}{f_{Ct}^{(i)}}\theta_{\hat{\imath}t}^2\tilde{\sigma}_t^2d\hat{\imath} - \eta_t\int_{\hat{\mathcal{I}}}\mathbb{E}_{\tilde{\nu}}\left[\frac{f_{C}^{(i)}(C_{it^-}e^{-\tilde{\zeta}_t\mathbf{1}_{\{i=\hat{\imath}\}}},\bigl\{\theta_{\hat{\imath}t^-}e^{-\tilde{\zeta}_t}\bigr\}_{\hat{\imath}\in\hat{\mathcal{I}}},X_{t^-})}{f_{C}^{(i)}(C_{it^-},\hat{\Theta}_{t^-},X_{t^-})}-1\right]d\hat{\imath}\\
 - \frac{f_{CX,t}^{(i)}}{f_{Ct}^{(i)}}\mu_{Xt} - \frac{1}{2}\frac{f_{CXX,t}^{(i)}}{f_{Ct}^{(i)}}|\sigma_{Xt}|^2  - \frac{f_{CCX,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}\sigma_{Ct}^{(i)\top}\sigma_{Xt} - \int_{\hat{\mathcal{I}}}\frac{f_{C\theta_{\hat{\imath}}X,t}^{(i)}}{f_{Ct}^{(i)}}\sigma_{\theta t}^{(\hat{\imath})\top}\sigma_{Xt}d\hat{\imath}.
\label{eq:riskfreerate1_pf_theory}
\end{multline*}$$ Multiplying both sides by $f_{Ct}^{(i)}/f_{CC,t}^{(i)}$, integrating over the support $\mathcal{I}$, and algebraically manipulating terms then yields the stated solution, where $$\begin{equation}
\Xi_{\hat{\Theta}t} = \int_{\hat{\mathcal{I}}}\gamma_{\theta_{\hat{\imath}}t}^{(A)}\theta_{\hat{\imath}t}\mu_{\theta t}^{(\hat{\imath})}d\hat{\imath} + \frac{1}{2}\int_{\hat{\mathcal{I}}}\int_{\hat{\mathcal{I}}}\gamma_{\theta_{\hat{\imath}}\theta_{\hat{\imath}'},t}^{(A)}\theta_{\hat{\imath}t}\theta_{\hat{\imath}'t}\sigma_{\theta t}^{(\hat{\imath})\top}\sigma_{\theta t}^{(\hat{\imath}')}d\hat{\imath}d\hat{\imath}' + \gamma_{Ct}^{(A)}\chi_{C\theta_{\hat{\imath}},t}^{(A)},
\label{eq:xishare_systematic}
\end{equation}$$ $$\begin{equation}
\tilde{\Xi}_{\hat{\Theta}t} = \frac{1}{2}\int_{\hat{\mathcal{I}}}\gamma_{\theta_{\hat{\imath}}\theta_{\hat{\imath}},t}^{(A)}\theta_{\hat{\imath}t}^2\tilde{\sigma}_t^2d\hat{\imath} - \eta_t\int_{\hat{\mathcal{I}}}\mathbb{E}_{\tilde{\nu}}\left[\tilde{\mathcal{J}}_{\theta_{\hat{\imath}}t}^{(A)}-1+\gamma_{\theta_{\hat{\imath}}t}^{(A)}\theta_{\hat{\imath}t}(e^{-\tilde{\zeta}_t}-1)]\right]d\hat{\imath},
\label{eq:xishare_idio}
\end{equation}$$ and $$\begin{equation}
\Xi_{Xt} =  \gamma_{Xt}^{(A)}\mu_{Xt} + \frac{1}{2}\gamma_{XX,t}^{(A)}|\sigma_{Xt}|^2 + \gamma_{Ct}^{(A)}\chi_{CX,t}^{(A)} + \gamma_{Ct}^{(A)}\chi_{\theta_{\hat{\imath}}X,t}^{(A)}.
\label{eq:xicrosssec}
\end{equation}$$ In ([\[eq:xishare_systematic\]](#eq:xishare_systematic)), we see two new variables that represent aggregates of preference elasticities: the aggregate sensitivity to systematic consumption-share shocks $\gamma_{\theta_{\hat{\imath}}\theta_{\hat{\imath}'}}^{(A)}$ and the aggregate sensitivity to the correlation of such consumption-share shocks with aggregate consumption shocks $\chi_{C\theta_{\hat{\imath}}}^{(A)}$. The aggregate preference elasticities $\gamma_{XX}^{(A)}$, $\chi_{CX}^{(A)}$, and $\chi_{\theta_{\hat{\imath}}X}^{(A)}$ are defined analogously. ◻

***Proof of Proposition 12**.* Applying Itô's lemma to the state-price density for agent $i$ and substituting into the riskfree rate equation ([\[eq:riskpremium_general_theory\]](#eq:riskpremium_general_theory)), we get $$\begin{multline*}
r_{St}-r_t = - \frac{f_{CC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}\sigma_{Ct}^{(i)\top}\sigma_{St} - \int_{\hat{\mathcal{I}}}\frac{f_{C\theta_{\hat{\imath}},t}^{(i)}}{f_{Ct}^{(i)}}\theta_{\hat{\imath}t}\sigma_{\theta t}^{(\hat{\imath})\top}\sigma_{St}d\hat{\imath} - \frac{f_{CX,t}^{(i)}}{f_{Ct}^{(i)}}\sigma_{Xt}^\top \sigma_{St} \\
- \sum_{j=1}^n\lambda^{(j)}\left[\left(\frac{f_{C}^{(i)}(C_{it^-}e^{-\zeta_{Ct}^{(i,j)}},\bigl\{\theta_{\hat{\imath}t^-}e^{\zeta_{\theta t}^{(\hat{\imath})}}\bigr\}_{\hat{\imath}\in\hat{\mathcal{I}}},X_{t^-}+\zeta_{Xt}^{(j)})}{f_{C}^{(i)}(C_{it^-},\hat{\Theta}_{t^-},X_{t^-})}-1\right)(e^{-\zeta_{St}^{(j)}}-1)\right].
\end{multline*}$$ As in the proof of the riskfree rate, multiply both sides by $f_{Ct}^{(i)}/f_{CC,t}^{(i)}$, integrate over the support $\mathcal{I}$, and algebraically manipulate terms to get the aggregated solution. ◻

***Proof of Lemma 6**.* Because of the assumption that $X$ and $C_i$ are Markov, each agent's value function takes the form $V_{it}=J^{(i)}(C_{it},\hat{\Theta}_t,X_t)$ and satisfies the partial differential (HJB) equation $$\begin{multline}
0 = J_C^{(i)}c_i\left(\mu_C^{(i)}(c_i,\hat{\theta},x) - \eta(x)\mathbb{E}_{\tilde{\nu}}\left[e^{-\tilde{\zeta}(x,\tilde{Z})}-1\right]\right) \\
+ \int_{\hat{\mathcal{I}}}J_{\theta_{\hat{\imath}}}^{(i)}\theta_{\hat{\imath}}\left(\mu_{\theta}^{(\hat{\imath})}(c_i,\hat{\theta},x)-\eta(x)\mathbb{E}_{\tilde{\nu}}\left[e^{-\tilde{\zeta}(x,\tilde{Z})}-1\right]\right)d\hat{\imath} + J_X^{(i)}\mu_X(x) \\
+ \frac{1}{2}J_{CC}^{(i)}c^2\left(|\sigma_C^{(i)}(c_i,\hat{\theta},x))|^2 + \tilde{\sigma}(x)^2\right) + \frac{1}{2}\int_{\hat{\mathcal{I}}}J_{\theta_{\hat{\imath}}\theta_{\hat{\imath}}}^{(i)}\theta_{\hat{\imath}}^2\tilde{\sigma}(x)^2d\hat{\imath}  + \frac{1}{2}J_{XX}^{(i)}|\sigma_X(x)|^2 \\
+ \frac{1}{2}\int_{\hat{\mathcal{I}}}\int_{\hat{\mathcal{I}}}J_{\theta_{\hat{\imath}}\theta_{\hat{\imath}'}}^{(i)}\theta_{\hat{\imath}}\theta_{\hat{\imath}'}\sigma_{\theta}^{(\hat{\imath})}(c_i,\hat{\theta},x)^\top\sigma_{\theta}^{(\hat{\imath}')}(c_i,\hat{\theta},x)d\hat{\imath}d\hat{\imath}' + J_{CX}^{(i)}c\sigma_C^{(i)}(c_i,\hat{\theta},x)^\top\sigma_X(x)  \\
+ \int_{\hat{\mathcal{I}}}J_{C\theta_{\hat{\imath}}}^{(i)}c_i\theta_{\hat{\imath}}\sigma_{C}^{(i)}(c_i,\hat{\theta},x)^\top\sigma_{\theta}^{(\hat{\imath})}(c_i,\hat{\theta},x)d\hat{\imath} + \int_{\hat{\mathcal{I}}}J_{\theta_{\hat{\imath}}X}^{(i)}\sigma_{\theta}^{(\hat{\imath})}(c_i,\hat{\theta},x)^\top\sigma_{X}(x)d\hat{\imath} \\
+ \eta(x)\int_{\hat{\mathcal{I}}}\mathbb{E}_{\tilde{\nu}}\left[J^{(i)}(c_ie^{-\tilde{\zeta}(x,\tilde{Z})\mathbf{1}_{\{i=\hat{\imath}\}}},\{\theta_{\hat{\imath}}e^{-\tilde{\zeta}^{(\hat{\imath})}(x,\tilde{Z})}\}_{\hat{\imath}\in\hat{\mathcal{I}}},x)-J^{(i)}(c_i,\hat{\theta},x)\right]d\hat{\imath} \\
+\sum_{j=1}^n\lambda^{(j)}\left[J^{(i)}(c_ie^{-\zeta_C^{(j)}(c_i,\hat{\theta},x)},\{\theta_{\hat{\imath}}e^{\zeta_\theta^{(\hat{\imath})}(c_i,\hat{\theta},x)}\}_{\hat{\imath}\in\hat{\mathcal{I}}},x+\zeta_{X}^{(j)}(x))-J^{(i)}(c_i,\hat{\theta},x)\right] \\
+ \eta(x)\mathbb{E}_{\tilde{\nu}}\left[J^{(i)}(c_ie^{-\tilde{\zeta}(x,\tilde{Z})},\hat{\theta},x)-J^{(i)}(c_i,\hat{\theta},x)\right] + \bar{f}^{(i)}(c_i,J^{(i)}(c_i,\hat{\theta},x)).
\label{eq:HJBpf_theory}
\end{multline}$$ Suppose first that $\bar{f}^{(i)}$ is not additively separable and $X$ is time-varying. In this case, $\partial\bar{f}^{(i)}(c,v)/\partial c$ is a function of both $c$ and $v$; therefore, after evaluating this derivative at $v=J^{(i)}(c,\hat{\theta},x)$, we know that marginal felicity is a function of cross-sectional risk if and only if $J^{(i)}(c,\hat{\theta},x)$ is in fact a function of $x$. Moreover, if cross-sectional risk is time-varying, we know that at least one of the coefficients $\tilde{\sigma}(x)$, $\eta(x)$, and $\tilde{\zeta}(x,\tilde{Z})$ is a function of the process $X$. Thus, the HJB equation ([\[eq:HJBpf_theory\]](#eq:HJBpf_theory)) implies that $J^{(i)}(c,\hat{\theta},x)$ is indeed a function of $x$, so marginal felicity $f_{Ct}^{(i)}$ depends on cross-sectional risk.

To complete the proof, it suffices to show that, if one of the conditions does not hold, then the marginal felicity function is not a function of cross-sectional risk. Evidently, if $\bar{f}^{(i)}(c,v)=u^{(i)}(c)+g^{(i)}(v)$, then $f_C^{(i)}(c,
\hat{\theta},x)=f_C^{(i)}(c)=\partial u^{(i)}(c)/\partial c$. Note that $u^{(i)}(c)$ must be differentiable by the assumption that $\bar{f}^{(i)}(c,v)$ is $C^{3,1}$, so this derivative is well-defined. Alternatively, if $X$ is not time-varying, then it is a constant and the HJB equation above simplifies to a PDE in $c_i$ and $\hat{\theta}$ only, so $f_C^{(i)}(c,\hat{\theta},x)=f_C^{(i)}(c,\hat{\theta})$. ◻

***Proof of Lemma 7**.* Suppose that all agents have additively separable preferences, so that marginal felicity $f_{Ct}^{(i)} = u_C^{(i)}(C_{it})$ for all $i\in\mathcal{I}$. Risk premia in the incomplete-market economy become $$\begin{equation}
r_{St}-r_t = - \frac{u_{CC,t}^{(i)}}{u_{Ct}^{(i)}}C_{it}\sigma_{Ct}^{(i)\top}\sigma_{St} + \sum_{j=1}^n\lambda^{(j)}\left[\left(\frac{u_C^{(i)}(C_{it^-}e^{-\zeta_{Ct}^{(i,j)}})}{u_C^{(i)}(C_{it^-})}-1\right)(1-e^{-\zeta_{St}^{(j)}})\right].
\label{eq:riskpremiumpartial_additive_theory}
\end{equation}$$ A condition of the exact same form holds in the complete-market economy. Because we take the current distribution of consumption as given, it must be that, for each agent $i$, $u_{Ct}^{(i)}$ is identical in the complete- and incomplete-market economies. Moreover, because we have assumed that agents can trade in $m+n$ non-redundant risky securities and because the condition ([\[eq:riskpremiumpartial_additive_theory\]](#eq:riskpremiumpartial_additive_theory)) is of the same form in both economies, the equilibrium values of $\sigma_{Ct}^{(i)}$ and $\zeta_{Ct}^{(i,j)}$ must be uniquely determined and the same in both economies.

Specifically, since there are $m+n$ non-redundant stocks, there exist $m+n$ non-redundant portfolios, $m$ of which are each exposed to only one of the Brownian motions and $n$ of which are exposed to one of the Poisson jumps. The risk premium ([\[eq:riskpremiumpartial_additive_theory\]](#eq:riskpremiumpartial_additive_theory)) and the corresponding aggregated version then imply that $\gamma_{Ct}^{(i)}\sigma_{Ct}^{(i)} = \gamma_{Ct}^{(A)}\sigma_C^{(A)}$ for both economies, as claimed. Moreover, equating agents' coefficients on Poisson jump $j$ implies $$\begin{equation}
\frac{u_C^{(i)}(C_{it^-}e^{-\zeta_{Ct}^{(i,j)}})}{u_C^{(i)}(C_{it^-})} = \frac{u_C^{(i')}(C_{i't^-}e^{-\zeta_{Ct}^{(i',j)}})}{u_C^{(i')}(C_{i't^-})}.
\label{eq:jumpsequated_theory}
\end{equation}$$ Because $u_C^{(i)}$ is assumed to be strictly decreasing and continuous, it has an inverse $u_C^{(i)-1}$ and we can conclude that $$C_{i't^-}e^{-\zeta_{Ct}^{(i',j)}}=u_C^{(i')-1}\left(u_C^{(i')}(C_{i't^-})\frac{u_C^{(i)}(C_{it^-}e^{-\zeta_{Ct}^{(i,j)}})}{u_C^{(i)}(C_{it^-})}\right).$$ Summing over agents $i'\in\mathcal{I}$ and imposing the fact that $\int_\mathcal{I}C_{i't^-}e^{-\zeta_{Ct}^{(i',j)}}di'=C_{t^-}e^{-\zeta_C^{(j)}}$ gives us the result.

Finally, notice that $\sigma_{Ct}^{(i)} = \sigma_C^{(A)}$ if and only if $\gamma_{Ct}^{(i)} = \gamma_{Ct}^{(A)}$, which itself can only be true for all consumption distributions if all agents have log or power utility with identical coefficients of relative risk aversion $\gamma$. Likewise, the condition ([\[eq:jumpsequated_theory\]](#eq:jumpsequated_theory)) suggests that $\zeta_{Ct}^{(i,j)} = \zeta_C^{(j)}$ for all consumption distributions if and only if the same preference condition holds. ◻

***Proof of Lemma 8**.* If preferences are additively separable, then $f_C^{(i)}(c)=u_C^{(i)}(c)$ for all agents $i\in\mathcal{I}$, and thus the riskfree rate reduces to $$\begin{multline*}
r_t = -f_{Vt}^{(i)}-\frac{f_{CC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}\mu_{Ct}^{(i)} -\frac{1}{2}\frac{f_{CCC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}^2|\sigma_{Ct}^{(i)}|^2 -\sum_{j=1}^n\lambda^{(j)}\left[\frac{f_{C}^{(i)}(C_{it^-}e^{-\zeta_{Ct}^{(i,j)}})}{f_{C}^{(i)}(C_{it^-})}-1\right]\\
-\frac{1}{2}\frac{f_{CCC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}^2(|\sigma_{Ct}^{(i)}|^2 + \tilde{\sigma}_t^2) - \eta_t \mathbb{E}_{\tilde{\nu}}\left[\frac{f_{C}^{(i)}(C_{it^-}e^{-\tilde{\zeta}_t})}{f_{C}^{(i)}(C_{it^-})}-1-\frac{f_{CC,t}^{(i)}}{f_{Ct}^{(i)}}C_{it}(e^{-\tilde{\zeta}_t}-1)\right].
\end{multline*}$$ By Lemma 7, the terms including $\sigma_{Ct}^{(i)}$ and $\zeta_{Ct}^{(i,j)}$ are the same whether markets are complete or incomplete. Notice, however, that $f_{Vt}^{(i)}=g_V^{(i)}(V_{it})$ in general might not equal $f_{Vt}^{{\rm CM}(i)}$, since the HJB equation from the proof of Lemma 6 implies that the value functions in the two economies will differ. Thus, upon aggregating in the usual fashion, we get the expression stated in the lemma. ◻

***Proof of Theorem 3**.* The sufficiency of these two conditions was proven by Theorem 2: if both of them hold, then risk premia are unchanged by stochastic cross-sectional risk. The necessity of the second condition also follows from identical logic as in the proof of Theorem 2: if aggregate consumption growth is correlated with cross-sectional risk, then it necessarily alters risk premia under any preferences.

To show the necessity of identical time-additive power or log utility, let us establish a few facts about the stock price. Note first that, using the arguments from Lemma 3, the price-dividend ratio solves the PDE $$\begin{multline}
F(c,\hat{\theta},x)^{-1}+\mathbb{E}_{\tilde{\nu}}\left[\mu_S(c,\hat{\theta},x)\right] + \sum_{j=1}^n\lambda^{(j)}\left[e^{-\zeta_S^{(j)}(c,\hat{\theta},x)}-1\right] - r(c,\hat{\theta},x) \\
= \left(\gamma_C^{(A)}(c,\hat{\theta},x)\sigma_C + \int_{\hat{\mathcal{I}}}\gamma_{\theta_{\hat{\imath}}}^{(A)}(c,\hat{\theta},x)\sigma_\theta^{(\hat{\imath})}(c,
\hat{\theta},x)d\hat{\imath} + \gamma_X^{(A)}(c,\hat{\theta},x)\sigma_X(x)\right)^\top\sigma_S(c,\hat{\theta},x) \\
+ \sum_{j=1}^n\lambda^{(j)}\left[\left(\mathcal{J}_{C\hat{\Theta}X}^{(A,j)}(c,\hat{\theta},x)-1\right)(1-e^{-\zeta_S^{(j)}(c,\hat{\theta},x)})\right],
\label{eq:equitypde_gentheory}
\end{multline}$$ Recognize also that, whenever $X$ is time-varying, the riskfree rate $r$ is a function of $X$ in the incomplete-market economy. Thus, from the PDE ([\[eq:equitypde_gentheory\]](#eq:equitypde_gentheory)), we can conclude that $F$ is a function of $X$ if and only if $X$ is time-varying. As a result, these stock-price coefficients depend on $\sigma_{Xt}$ and $\zeta_{Xt}^{(j)}$, and it must be that $X$ is correlated with the stock: either $\sigma_{Xt}^\top\sigma_{St}\neq0$, $\zeta_{Xt}^{{(j)}\top}\zeta_{St}^{(j)}\neq0$ for some $j$, or multiple of these. In the complete-market economy, however, $F$ is independent of $X$, and thus so are the equity-risk coefficients.

From Lemma 6 and the fact that $X$ is correlated with $S$, we know that agents demand a premium for stochastic cross-sectional risk if and only if they have non-additively-separable preferences. The argument is similar to that in the proof of Theorem 1. Hence, irrelevance implies all agents have additively separable preferences. Assuming separability and using the riskfree rate relation from Lemma 8, the incomplete-market risk premium implies that the stock's price-dividend ratio solves the differential equation $$\begin{multline}
F_t^{-1}+\mathbb{E}_{\tilde{\nu}}\left[\mu_{St}\right] + \sum_{j=1}^n\lambda^{(j)}\left[e^{-\zeta_{St}^{(j)}}-1\right] \\
- r_t^{\rm CM} - (f_{Vt}^{{\rm CM}(A)}-f_{Vt}^{(A)}) + \frac{1}{2}\gamma_{Ct}^{(A)}\tilde{\xi}_t^{(A)} + \eta_t \mathbb{E}_{\tilde{\nu}}\left[\tilde{\mathcal{J}}_{Ct}^{(A)}-1+\gamma_{Ct}^{(A)}(e^{-\tilde{\zeta}_t}-1)\right] \\
= \gamma_{Ct}^{(A)}\sigma_C^\top\sigma_{St} + \sum_{j=1}^n\lambda^{(j)}E_{\nu_{CXD}^{(j)}}\left[\left(\mathcal{J}_{Ct}^{(A,j)}-1\right)(1-e^{-\zeta_{St}^{(j)}})\right].
\label{eq:stockpde_proof_theory}
\end{multline}$$ In order to prove the claim, suppose for the sake of contradiction that agents do not have identical power or log utility, but that risk premia are identical in the complete- and incomplete-market economies. By the last statement in Lemma 7, it must be that $\sigma_{\theta t}^{(\hat{\imath})}\neq0$ and $\zeta_{\theta t}^{(\hat{\imath},j)}\neq0$ for a positive measure of agents $\hat{\imath}\in\hat{\mathcal{I}}$. This has two important implications. First, it means that the riskfree rate is a function of the consumption shares $\hat{\Theta}_t$, so $F_t$ is indeed a function of these shares. Second, it means that the only way in which risk premia can be the same in the complete and incomplete markets is if $F_{Ct}/F_t=F_{Ct}^{\rm CM}/F_t^{\rm CM}$, $F_{\theta_{\hat{\imath}}t}/F_t=F_{\theta_{\hat{\imath}}t}^{\rm CM}/F_t^{\rm CM}$, and $$\frac{F(C_{t^-}e^{-\zeta_C^{(j)}},\bigl\{\theta_{\hat{\imath}t^-}e^{\zeta_{\theta t}^{(\hat{\imath},j)}}\bigr\}_{\hat{\imath}\in\hat{\mathcal{I}}},X_{t^-}+\zeta_{Xt}^{(j)})}{F(C_{t^-},\hat{\Theta}_{t^-},X_{t^-})} = \frac{F^{\rm CM}(C_{t^-}e^{-\zeta_C^{(j)}},\bigl\{\theta_{\hat{\imath}t^-}e^{\zeta_{\theta t}^{(\hat{\imath},j)}}\bigr\}_{\hat{\imath}\in\hat{\mathcal{I}}})}{F^{\rm CM}(C_{t^-},\hat{\Theta}_{t^-})}.$$ Now, since we assumed that risk premia were the same in both economies, we can substitute these complete-market quantities into the left-hand side of the differential equation ([\[eq:stockpde_proof_theory\]](#eq:stockpde_proof_theory)) and set the whole expression equal to the corresponding expression in the complete market. Doing so and removing terms that are identical on both sides of the expression yields the following: $$\begin{multline}
0 = F_t^{-1} - (F_t^{\rm CM})^{-1} + \frac{F_{Xt}}{F_t}(\mu_{Xt}+\sigma_D^\top\sigma_{Xt}) + \frac{1}{2}\frac{F_{XX,t}}{F_t}|\sigma_{Xt}|^2 \\
+ \int_{\hat{\mathcal{I}}}\frac{F_{\theta_{\hat{\imath}}t}}{F_t}\theta_{\hat{\imath}t}\left(\mu_{\theta t}^{(\hat{\imath})}-\mu_{\theta t}^{{\rm CM}(\hat{\imath})}-\eta_t(e^{-\tilde{\zeta}_t}-1)\right)d\hat{\imath} + \frac{1}{2}\int_{\hat{\mathcal{I}}}\frac{F_{\theta_{\hat{\imath}}\theta_{\hat{\imath}},t}}{F_t}\theta_{\hat{\imath}t}^2\tilde{\sigma}_t^{(\hat{\imath})2}d\hat{\imath}  \\
 + \eta_t \int_{\hat{\mathcal{I}}}\mathbb{E}_{\tilde{\nu}}\left[\frac{F(C_{t^-},\bigl\{\theta_{\hat{\imath}t^-}e^{-\tilde{\zeta}_t}\bigr\}_{\hat{\imath}\in\hat{\mathcal{I}}},X_{t^-})}{F(C_{t^-},\hat{\Theta}_{t^-},X_{t^-})}-1\right]d\hat{\imath}\\
- (f_{Vt}^{{\rm CM}(A)}-f_{Vt}^{(A)}) + \frac{1}{2}\gamma_{Ct}^{(A)}\tilde{\xi}_t^{(A)} + \eta_t\mathbb{E}_{\tilde{\nu}}\left[\tilde{\mathcal{J}}_{Ct}^{(A)}-1+\gamma_{Ct}^{(A)}(e^{-\tilde{\zeta}_t}-1)\right].
\label{eq:impliedpde_proof_theory}
\end{multline}$$ Herein lies the contradiction. Our assumption that risk premia were equivalent implied that $F_{\theta_{\hat{\imath}}t}/F_t=F_{\theta_{\hat{\imath}}t}^{\rm CM}/F_t^{\rm CM}$, which means it is necessarily the case that $F_{\theta_{\hat{\imath}}t}/F_t$ and $F_{\theta_{\hat{\imath}}\theta_{\hat{\imath}},t}/F_t$ are independent of $X$. However, since $X$ is time-varying and at least one of the elements of $\{\tilde{\sigma}_t,\eta_t,\tilde{\zeta}_t\}$ depends on $X$, the differential equation ([\[eq:impliedpde_proof_theory\]](#eq:impliedpde_proof_theory)) implies that $F_{\theta_{\hat{\imath}}t}/F_t$ is in fact a function of $X$. By way of this contradiction, we have proven that identical power or log utility is a necessary condition for irrelevance.

What is the intuition for this proof by contradiction? We have shown that, if agents do not have identical isoelastic and homothetic preferences, then the equity valuation $F$, and therefore the equity-risk coefficients, is affected by both consumption shares and cross-sectional risk. Agents demand compensation for these consumption-share shocks (they are just scaled exposures to systematic consumption shocks), so it shows up in the risk premium differently in an incomplete market. ◻

Aiyagari, S. Rao. 1994. "Uninsured Idiosyncratic Risk and Aggregate Saving." *The Quarterly Journal of Economics* 109 (3): 659--84.

Basak, Suleyman, and Domenico Cuoco. 1998. "An Equilibrium Model with Restricted Stock Market Participation." *The Review of Financial Studies* 11 (2): 309--41.

Bewley, Truman. 1986. "Stationary Monetary Equilibrium with a Continuum of Independently Fluctuating Consumers." In *Contributions to Mathematical Economics in Honor of Gérard Debreu*, edited by W. Hildenbrand and A. Mas-Collel. North-Holland Amsterdam.

Brav, Alon, George M. Constantinides, and Christopher C. Geczy. 2002. "Asset Pricing with Heterogeneous Consumers and Limited Participation: Empirical Evidence." *Journal of Political Economy* 110 (4): 793--824.

Brunnermeier, Markus K., and Yuliy Sannikov. 2014. "A Macroeconomic Model with a Financial Sector." *American Economic Review* 104 (2): 379--421.

Catherine, Sylvain. 2020. "Countercyclical Labor Income Risk and Portfolio Choices over the Life-Cycle." Unpublished manuscript.

Cochrane, John H. 2008. "The Dog That Did Not Bark: A Defense of Return Predictability." *The Review of Financial Studies* 21 (4): 1533--75.

Constantinides, George M., and Anisha Ghosh. 2017. "Asset Pricing with Countercyclical Household Consumption Risk." *The Journal of Finance* 72 (1): 415--60.

Cont, Rama, and Peter Tankov. 2004. *Financial Modelling with Jump Processes*. Chapman & Hall/CRC Financial Mathematics Series.

Cox, John C., Jonathan E. Ingersoll, and Stephen A. Ross. 1985. "A Theory of the Term Structure of Interest Rates." *Econometrica* 53 (2): 385--407.

Duffie, Darrell. 2010. *Dynamic Asset Pricing Theory*. Princeton University Press.

Duffie, Darrell, and Larry G. Epstein. 1992. "Asset Pricing with Stochastic Differential Utility." *The Review of Financial Studies* 5 (3): 411--36.

Farhi, Emmanuel, and François Gourio. 2018. "Accounting for Macro-Finance Trends: Market Power, Intangibles, and Risk Premia." *Brookings Papers on Economic Activity*, 147--250.

Gârleanu, Nicolae, and Stavros Panageas. 2015. "Young, Old, Conservative, and Bold: The Implications of Heterogeneity and Finite Lives for Asset Pricing." *Journal of Political Economy* 123 (3): 670--85.

Gomez, Matthieu, and Émilien Gouin-Bonenfant. 2020. "A q-Theory of Inequality." Unpublished manuscript.

Guvenen, Fatih, Serdar Ozkan, and Jae Song. 2014. "The Nature of Countercyclical Income Risk." *Journal of Political Economy* 122 (3): 621--60.

He, Zhiguo, and Arvind Krishnamurthy. 2013. "Intermediary Asset Pricing." *American Economic Review* 103 (2): 732--70.

Huggett, Mark. 1993. "The Risk-Free Rate in Heterogeneous-Agent Incomplete-Insurance Economies." *Journal of Economic Dynamics and Control* 17 (5): 953--69.

Kaplan, Greg, Benjamin Moll, and Giovanni L. Violante. 2018. "Monetary Policy According to HANK." *American Economic Review* 108 (3): 697--743.

Kimball, Miles S. 1990. "Precautionary Saving in the Small and in the Large." *Econometrica* 58 (1): 53--73.

Koijen, Ralph, Stijn Van Nieuwerburgh, and Roine Vestman. 2014. "Judging the Quality of Survey Data by Comparison with "Truth\" as Measured by Administrative Records: Evidence from Sweden." In *Improving the Measurement of Consumer Expenditures*. University of Chicago Press.

Martin, Ian W R. 2013. "Consumption-Based Asset Pricing with Higher Cumulants." *Review of Economic Studies* 80 (2): 745--73.

Mehra, Rajnish, and Edward C. Prescott. 1985. "The Equity Premium: A Puzzle." *Journal of Monetary Economics* 15 (2): 145--61.

Miller, Max, James D. Paron, and Jessica A. Wachter. 2021. "Sovereign Default and the Decline in Interest Rates." Unpublished manuscript.

Panageas, Stavros. 2020. "The Implications of Heterogeneity and Inequality for Asset Pricing: A Survey." Unpublished manuscript.

Protter, Philip. 1992. *Stochastic Integration and Differential Equation*. Second. Springer-Verlag.

Schmidt, Lawrence D. W. 2015. "Climbing and Falling Off the Ladder: Asset Pricing Implications of Labor Market Event Risk." Unpublished manuscript.

Shiller, Robert J. 1981. "Do Stock Prices Move Too Much to Be Justified by Subsequent Changes in Dividends?" *The American Economic Review* 71 (3): 421--36.

Smith, Matthew, Danny Yagan, Owen Zidar, and Eric Zwick. 2019. "Capitalists in the Twenty-First Century." *The Quarterly Journal of Economics* 134 (4): 1675--745.

Tsai, Jerry, and Jessica A. Wachter. 2018. "Pricing Long-Lived Securities in Dynamic Endowment Economies." *Journal of Economic Theory* 177: 848--78.

Viceira, Luis M. 2001. "Optimal Portfolio Choice for Long-Horizon Investors with Nontradable Labor Income." *The Journal of Finance* 56 (2): 433--70.

[^1]: Department of Finance, The Wharton School, University of Pennsylvania. Email: jparon@wharton.upenn.edu.

[^2]: I thank Hengjie Ai, Jules van Binsbergen, Sylvain Catherine, Domenico Cuoco, Winston Dou, Maria Gelrud, Joachim Hubmer, Tim Landvoigt, Max Miller, Nick Roussanov, Tom Sargent, Larry Schmidt, Jessica Wachter, and seminar participants at the Wharton School for helpful comments.

[^3]: Countercyclical risk means countercyclical variance, skewness, or some higher moment of the cross-sectional shock distribution. show that countercyclicality is essential for generating a risk premium in discrete-time models like, for instance, that of .

[^4]: Articles arguing for the relevance of jumps include and .

[^5]: find that three-quarters of pass-through profits accruing to top earners are inalienable human capital income. Indeed, this human capital component of entrepreneurial income exceeds income from public equity.

[^6]: Empirical tests of incomplete-market models have yielded mixed results. Using panel data on consumption and income, some have found that observed income left-skewness is enough to explain the data (Brav et al. 2002; Schmidt 2015; Constantinides and Ghosh 2017). However, argues that, because the wealth share of agents with high income-wealth ratios is low compared to the wealth share of older equity owners, uninsurable labor income risk is negligible for risk premia. This analysis excludes the human capital component of business income (Smith et al. 2019), captured by my model.

[^7]: constructs a framework that accommodates market incompleteness given time-additive utility and Brownian (Gaussian) risks. Under his approach, the first type of incompleteness is also considered a "portfolio constraint,\" where the constraint is missing (non-tradeable) assets.

[^8]: This is not as restrictive as it might seem: all that is required is the assumption that there exists a fixed subset of investors in the economy who are always unconstrained. In other words, it does not require that *every* person in an economy is unconstrained or even a stock owner.

[^9]: *Because $\eta$ is stochastic, $N_i$ is technically a Cox process. I refer to it as a Poisson process for simplicity and to keep with convention in the literature.*

[^10]: *Because the Poisson processes $N^{(j)}$ and $N_i$ have a countable number of jumps almost surely, the integrals $\int\mu_X(X_t)dt$ and $\int\mu_X(X_{t^-})dt$ differ only on a set of measure zero. The same is true of the stochastic integrals $\int\sigma_X(X_t)^\top dB_t$ and $\int\sigma_X(X_{t^-})^\top dB_t$. We can therefore omit the superscripts on $t^-$ for corresponding coefficients of stochastic differential equations like ([\[eq:dcrossrisk_setup\]](#eq:dcrossrisk_setup)).*

[^11]: The use of a single systematic jump with randomly distributed size is the convention in aggregate disaster models like that of . The quantitative model in Section 3 switches to this case, without loss of generality, to make it easier to map to the disaster data.

[^12]: We could have begun by assuming agents' endowments, then permitting trade; however, this assumption would mean the framework excludes production economies. Examining equilibrium consumption covers both endowment and production economies without needing further assumptions on income and technologies.

[^13]: Since agents are atomistic, we could interpret $C_t$ as either "aggregate\" or "per-capita\" consumption.

[^14]: This claim takes for granted the fact that $V_{it}$ does not depend on the distribution of consumption shares $\Theta_t$. In actuality, we begin with the fact that $V_{it}=J(C_{it},\Theta_t,X_t)$ and prove that $\Theta_t$ is not a state variable, because preferences are identical and isoelastic.

[^15]: For example, consider an economy in which only a few assets are traded but all agents are endowed with an optimal consumption plan. In this case, we have an autarkic, incomplete-market equilibrium. State-price densities are equal and traded asset returns are equivalent to those in a corresponding complete market.

[^16]: In other words, the incomplete-market economy is the subset of *essentially incomplete* economic settings.

[^17]: use the term "generalized risk sensitivity\" to describe this property of marginal felicity, and derive complementary economic conclusions pertaining to other contexts.

[^18]: The statement of , for example, is that risk premia depend only on the covariance of equity-price shocks with aggregate consumption shocks, as in a standard complete market. Returns are held fixed across the complete- and incomplete-market economies.

[^19]: How do we know that the semi-elasticity $F_X/F$ is non-zero in this case? In an incomplete market, the riskfree rate always depends on cross-sectional risk $X$. Consequently, the price of the stock depends explicitly on $X$, varying whenever $X$ varies, so $F$ is indeed a non-trivial function of $X$.

[^20]: See for a detailed textbook treatment.

[^21]: I say "in principle\" because there is evidence that household-level consumption data may be of low quality (Koijen et al. 2014), limiting the validity of such direct empirical tests.

[^22]: We can think of the affine economy as an approximation of the full isoelastic economy if we take first-order Taylor expansions of the true coefficients.

[^23]: This concave investment function captures the possibility of adjustment costs that may render the yield on investment less than one-for-one. Note that $\lim_{\varphi\to0}\Phi(x_{it})=x_{it}$; therefore, the case of $\varphi=0$ represents no adjustment costs. use a function with similar properties.

[^24]: This is similar to the source of risk assumed by several production economies, including , , and .

[^25]: To be specific, $B_{Ht}$ and $B_{it}$ are standard Brownian motions; $N_{Ht}$ and $N_{it}$ are standard Poisson processes with intensities $\lambda$ and $\eta_t$, respectively. Again, all of these processes are independently distributed both over time and of each other.

[^26]: In the generalized framework, we denoted cross-sectional risk by $X$ and let $\eta_t=\eta(X_t)$. Now, we have that $X$ and $\eta$ are identical, and so I henceforth simply refer to $\eta$ instead of $X$.

[^27]: A related literature studies the distributional and aggregate implications of exactly this kind of heterogeneity (Gomez and Gouin-Bonenfant 2020). However, much of this literature takes returns as given or abstracts from characteristics like risk, missing the feedback between decisions and asset returns. The setup of this model presents a tractable way in which to understand these phenomena in general equilibrium.

[^28]: We could just as easily define the market dividend as the claim to levered aggregate consumption (output after reinvestment) $C_t^\phi=(a-x)^\phi H_t^\phi$. Returns on this alternative claim will be exactly the same. Indeed, the dividend need not be a function of aggregate output at all; it could be modeled as some exogenous process.

[^29]: That said, there is nothing preventing, say, agent $i$ from going long the stock and agent $i'$ from going short by an equal amount.

[^30]: The intuition for this is that we have assumed a unit EIS and ex ante identical agents. Of course, this will not always be the case. A more general approach that does not rely on conjecture would be to recognize that $q_{it}=q_i(H_{it},\eta_t)$, so that $$dq_{it} = \mu_{qt}^{(i)}dt +\sigma_{qt}^{(i)\top}[dB_{Ht},dB_{\eta t}]^{\top} + (e^{\zeta_{qt}^{(i)}}-1) dN_{Ht}+\tilde{\sigma}_{qt}^{(i)}dB_{it} + (e^{\tilde{\zeta}_{qt}^{(i)}}-1)dN_{it}.$$ This fact can then be used to calculate the capital gains rate and find the unique solution for $q_{it}$.

[^31]: In the notation in Appendix 8, $\mu_{Xt}=\kappa_\eta\bar{\eta}-\kappa_\eta\eta_t$ and $|\sigma_{Xt}|^2=\sigma_\eta^2\eta_t$. Thus, a square-root process indeed implies that coefficients are affine in the state variable $\eta$.

[^32]: Every result here can also be derived from the conditions of the stochastic control problem we just solved.

[^33]: This is much less sensitive than the interest rate that prevails in models with time-varying aggregate disaster risk, in large part because I assume idiosyncratic disasters to be much smaller in magnitude: a decline of about 10% in my model versus 25% aggregate disasters in the data.

[^34]: Because we are considering the U.S. post-war experience, I assume that there are no aggregate disaster realizations in the sample.

[^35]: The Sharpe ratio is countercyclical because, roughly speaking, the risk premium increases in proportion to $\eta$, while volatility increases in proportion to $\sqrt{\eta}$. In some valid alternative calibrations of the model, this Sharpe ratio is initially flat for lower values of $\eta$ before it begins increasing; this stark nonlinearity is a common result in intermediary asset pricing models (He and Krishnamurthy 2013).

[^36]: refer to this measurement issue in asset pricing models as "dark matter.\"

[^37]: employs a similar procedure.

[^38]: A large macro-finance literature studies secular changes in asset pricing quantities like the price-dividend ratio (Farhi and Gourio 2018; Miller et al. 2021). Since the human-capital model does not allow for persistent or secular changes in macroeconomic variables like output growth, it abstracts from these important facts.

[^39]: The trends in this series are not very sensitive to the assumption of two-year income. Larger and smaller time horizons tell the same quantitative story.

[^40]: also report one-year income skewness from the SSA data. This shorter time horizon likely includes a large transitory component not captured in the human-capital model.

[^41]: This is not the first instance in which this controversy has arisen. A recent example is the response of to . point out that periodic endowment destruction is welfare-improving in habit models, because it increases future surplus consumption. dispute this claim by showing that this result is "fragile,\" in that its validity is contingent on the way in which the model is discretized.

[^42]: These studies are often based on the Aiyagari-Bewley-Huggett model (Aiyagari 1994; Bewley 1986; Huggett 1993). In a recent article, present a heterogeneous-agent framework characterizing the dynamics of the income and wealth distributions. Heterogeneous-agent models have also been proposed as alternatives to conventional new-Keynesian models (Kaplan et al. 2018). Furthermore, identify sources of rising wealth inequality in the U.S., finding that heterogeneous portfolio choices are a key factor. Indeed, in his comment on their paper, emphasizes that endogenizing asset prices is critical for understanding these issues.

[^43]: Thus, while one might find reason to object to the restrictions imposed on coefficients in this setting, the analytical solution admitted by them provides valuable intuition that can inform numerical solutions in more complicated economic settings.

[^44]: One may wonder whether the approximation in the case that the EIS $\psi\neq1$ is reasonably accurate in a jump-diffusion setting like this one. show that it is: in a complete-market economy that yields a solution similar to this one, the analytical approximations are close to a numerical solution of the full non-linear system.

[^45]: The second of these ODEs is a Riccati equation with constant coefficients and thus has a known explicit solution. The ways in which we can express this solution will depend on the parameter values, so I defer writing this explicit solution until the model in Section 3, where I put economically meaningful restrictions on the parameter space.

[^46]: When might we need to define such a subset? An example is the heterogeneous-agent model of , which includes two types of agents (types $\mathcal{A}$ and $\mathcal{B}$), differing in their risk aversion and elasticities of intertemporal substitution. In this model, $\hat{\Theta}$ consists of type-$\mathcal{A}$ agents' consumption shares.

[^47]: Lemma 2, on the other hand, no longer holds generally.

[^48]: Alternatively, we can interpret $\gamma_{C}^{(i)}$ as the (negative) elasticity of marginal felicity with respect to consumption: roughly, the percent increase in marginal felicity in response to a percent decrease in consumption.

[^49]: Notice that, in the case of identical power utility agents, $\omega_t^{(i)}$ is simply the consumption weight $C_{it}/C_t$.

[^50]: Given any sort of time-additive utility with rates of time preference $\rho^{(i)}$, this represents *aggregate impatience* $-f_{Vt}^{(A)}=\rho_t^{(A)}=\int_\mathcal{I}\omega_t^{(i)}\rho^{(i)}di$; for non-time-additive preferences, the interpretation is more complex.

[^51]: The use of a semi-elasticity, as opposed to an elasticity, makes intuitive sense because $X$ is naturally interpreted as stationary. As a result, we are interested in sensitivity to total changes, not percent changes.

[^52]: *Technically, all right-hand-side quantities should have a "CM\" superscript. I suppress these superscripts when clear.*

[^53]: Note that "all agents\" means a unit measure of agents, since we can ignore any measure-zero subset. Note also that "identical power utility\" means power utility with homogeneous coefficients of relative risk aversion $\gamma$ --- agents with identical power utility may still have heterogeneous rates of time preference $\rho^{(i)}$.

[^54]: Theorem 1 also generalizes in a similar way. In that case, additive separability replaces time-additive power utility as the necessary and sufficient condition.
